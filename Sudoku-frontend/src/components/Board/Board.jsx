import React, { useEffect, useState } from 'react';
import axios from 'axios'; //npm i axios
import Cell from './Cell';
import '../../App.css'; // Corrected import path for App.css

const Board = ({hintRequested, setHintRequested, selectedDifficulty}) => {
  // Store the board
  const [board, setBoard] = useState(Array(9).fill(Array(9).fill('')));
  const [selectedCell, setSelectedCell] = useState({ x: -1, y: -1 });
  // Store the solved board
  const [solved, setSolved] = useState(Array(9).fill(Array(9).fill('')));
  const [hintFound, setHintFound] = useState(false); // State to track if a hint is found

  useEffect(() => {
    const initializeBoardFromFile = async (filePath) => {
      try{
        //get information from json file
        const response = await axios.get(filePath);
        const data = response.data; //store jsondata

        //filter so 0 values are empty cells
        const filteredBoard = data.puzzle.map(row =>
          row.map(cell => (cell !== 0 ? cell : ''))
        )
        //add the user board as well as the solved one
        setBoard(filteredBoard);
        setSolved(data.solvedPuzzle);
      } catch (error){
        console.error("Error fetching", error)
      }
    }
    
    const url = "http://127.0.0.1:5000/api/load_puzzle" + selectedDifficulty;
    initializeBoardFromFile(url);
  }, [selectedDifficulty]);

  // Attempt to use backend GetHint. Not working yet
  // useEffect(() => {
  //   if(hintRequested && !hintFound){
  //     const randomHint = async (filePath) => {
  //       try{
  //         console.log(board);
  //         const response = await axios.get(filePath);
  //         const data = response.data; //store jsondata

  //         //filter so 0 values are empty cells
  //       const filteredBoard = data.puzzle.map(row =>
  //         row.map(cell => (cell !== 0 ? cell : ''))
  //       )
  //       //add the user board as well as the solved one
  //       setBoard(filteredBoard);
  //       setSolved(data.solvedPuzzle);
  //       console.log(board);
  //       } catch (error){
  //         console.error("Error fetching", error);
  //       }
  //     }
  //     randomHint('http://127.0.0.1:5000/api/hint');
  //     }
  //   setHintFound(false);
  //   setHintRequested(false);
  // }, []);

  useEffect(() => {
    // Everytime hint is requested in main App.jsx
    if(hintRequested && !hintFound){
      // Loops through the board until an empty cell is found
      for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[i].length; j++) {
          if(board[i][j] == 0){
            //get correct cell value from the solved board and pass it to board
            const hintValue = solved[i][j];
            // Call the cell change function to input changes
            handleCellChange(i,j, hintValue);
            setHintFound(true);
            setHintRequested(false);
            return;
          }

        }
      }
      // If all cell is fill request is set back to false
      if(!hintFound){
        setHintRequested(false);
      }
    }
    // Set found back to false for the next hint
    setHintFound(false);

  }, [hintRequested, hintFound, setHintRequested]);
  


  const handleCellChange = (x, y, value) => {
    setBoard(prevBoard => {
      const newBoard = prevBoard.map((row, rowIndex) =>
      rowIndex === x ? row.map((cell, cellIndex) =>
        cellIndex === y ? value : cell
      ) : row
    );
    //Convert the new changed board in a 2d grid
    const backBoard = Array.from(newBoard.values()).map((row) => row.map(Number));
    // Compare inputted cell to correct cell in solved Board
    const isCorrect = JSON.stringify(backBoard[x][y]) === JSON.stringify(solved[x][y]);
    // If the cell input is correct update database
    if(isCorrect){
      axios.post('http://127.0.0.1:5000/api/update', {puzzle: backBoard})
      return newBoard;
    }
    else{
      return prevBoard;
    }
  });
  };

  const handleCellSelect = (x, y) => {
    setSelectedCell({ x, y });
  };

  const isCellSelected = (x, y) => {
    return selectedCell.x === x && selectedCell.y === y;
  };

  const isSameRowOrColumnOrBox = (x, y) => {
    return (
      selectedCell.x === x || selectedCell.y === y ||
      (Math.floor(selectedCell.x / 3) === Math.floor(x / 3) &&
       Math.floor(selectedCell.y / 3) === Math.floor(y / 3))
    );
  };

  return (
    <div className="board">
      {board.map((row, x) => (
        <div key={x} className={`board-row ${x % 3 === 0 && x !== 0 ? 'thick-top' : ''}`}>
          {row.map((value, y) => (
            <Cell 
              key={`${x}-${y}`}
              value={value}
              rowIndex={x}
              colIndex={y}
              onChange={handleCellChange} 
              onSelect={handleCellSelect}
              isHighlighted={isSameRowOrColumnOrBox(x, y)}
              isSelected={isCellSelected(x, y)}
            />
          ))}
        </div>
      ))}
    </div>
  );
};

export default Board;

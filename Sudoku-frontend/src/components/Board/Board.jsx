import React, { useEffect, useState } from 'react';
import axios from 'axios'; 
import Cell from './Cell';
import '../../App.css'; 
// update made by Sou
// start : code added by manali 
const Board = ({selectedDifficulty, selectedBoard, hintRequested, setHintRequested, undoClicked, setUndoClicked, undoUntilCorrect, setUndoUntilCorrect}) => {
  // Store the board
  const [board, setBoard] = useState(Array(Number(selectedBoard)).fill(Array(Number(selectedBoard)).fill('')));
  const [selectedCell, setSelectedCell] = useState({ x: null, y: null });
  // Store the solved board
  const [solved, setSolved] = useState(Array(Number(selectedBoard)).fill(Array(Number(selectedBoard)).fill('')));
  const [hintFound, setHintFound] = useState(false); // State to track if a hint is found

  useEffect(() => {
    setBoard(Array(Number(selectedBoard)).fill(Array(Number(selectedBoard)).fill('')));
    setSolved(Array(Number(selectedBoard)).fill(Array(Number(selectedBoard)).fill('')));
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
        console.error("Error fetching", error);
      }
    }

    const url = "http://127.0.0.1:5000/api/load_board?difficulty=" + selectedDifficulty + "&size=" + Number(selectedBoard);
    initializeBoardFromFile(url);
  }, [selectedDifficulty, selectedBoard]);

  // // Attempt to use backend GetHint. Not working yet
  // useEffect(() => {
  //   if(hintRequested && !hintFound){
  //     const randomHint = async (filePath) => {
  //       try{
  //         // console.log(board);
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
  // }, [hintRequested, hintFound, setHintRequested]);

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
  
  useEffect(() => {
    const undo = async ()=>{
      // If the undo btn is clicked
      if(undoClicked){
        //Fetch the func undoing the move
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/undo/');
          const data = response.data; //store jsondata

          //filter so 0 values are empty cells
          const filteredBoard = data.puzzle.map(row =>
            row.map(cell => (cell !== 0 ? cell : ''))
          )
          //add the user board as well as the solved one
          setBoard(filteredBoard);
        } catch (error){
          console.error("Error fetching", error);
        }
        setUndoClicked(false); //Set the undobutton clicked back to false
    }
    };
    undo();
  }, [undoClicked, setUndoClicked]);

  useEffect(() => {
    const undoUntil = async ()=>{
      // If the undo btn is clicked
      if(undoUntilCorrect){
        //Fetch the func undoing the move
        try{
          const response = await axios.get('http://127.0.0.1:5000/api/undoUntilCorrect/');
          const data = response.data; //store jsondata

          //filter so 0 values are empty cells
          const filteredBoard = data.puzzle.map(row =>
            row.map(cell => (cell !== 0 ? cell : ''))
          )
          //add the user board as well as the solved one
          setBoard(filteredBoard);
        } catch (error){
          console.error("Error fetching", error);
        }
        setUndoUntilCorrect(false); //Set the undobutton clicked back to false
    }
    };
    undoUntil();
  }, [undoUntilCorrect, setUndoUntilCorrect]);

// By Nashrah
  const handleCellChange = (x, y, value) => {
    setBoard(prevBoard => {
      const newBoard = prevBoard.map((row, rowIndex) =>
      rowIndex === x ? row.map((cell, cellIndex) =>
        cellIndex === y ? value : cell
      ) : row
    );
    //Convert the new changed board in a 2d grid
    const backBoard = Array.from(newBoard.values()).map((row) => row.map(Number));
    
    axios.post('http://127.0.0.1:5000/api/update/', {puzzle: backBoard, new: backBoard[x][y], row: x, col: y})
      return newBoard;
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
      (Math.floor(selectedCell.x / Math.sqrt(Number(selectedBoard))) === Math.floor(x / Math.sqrt(Number(selectedBoard))) && 
      Math.floor(selectedCell.y / Math.sqrt(Number(selectedBoard))) === Math.floor(y / Math.sqrt(Number(selectedBoard))))
    );
  };
  const handleNumberSelect = (number) => {
    if (selectedCell.x != null && selectedCell.y != null) {
      handleCellChange(selectedCell.x, selectedCell.y, number.toString());
    }
  };  
  
  return (
    <div className={`board ${selectedBoard === '9' ? 'nine-grid' : 'four-grid'}`}>
      {board.map((row, x) => (
        <div key={x} className={`board-row ${x % Math.sqrt(Number(selectedBoard)) === 0 && x !== 0 ? 'thick-top' : ''}`}>
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
      <div className="number-pad">
      {Array.from({ length: selectedBoard === '9' ? 9 : 4 }, (_, i) => i + 1).map(number => (
        <button
          key={number}
          onClick={() => handleNumberSelect(number)}
          className="number-button"
        >
          {number}
        </button>
      ))}
    </div>
    </div>
  );
};
/*end : code added by manali */
export default Board;

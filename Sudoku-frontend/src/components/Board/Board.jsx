import React, { useEffect, useState } from 'react';
import axios from 'axios'; //npm i axios
import Cell from './Cell';
import '../../App.css'; // Corrected import path for App.css

const Board = () => {
  const [board, setBoard] = useState(Array(9).fill(Array(9).fill('')));
  const [selectedCell, setSelectedCell] = useState({ x: -1, y: -1 });

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
        //add the board
        setBoard(filteredBoard);
      } catch (error){
        console.error("Error fetching", error)
      }
    }
    initializeBoardFromFile('http://127.0.0.1:5000/api/get_puzzle/1')
  }, []);


  const handleCellChange = (x, y, value) => {
    setBoard(prevBoard => {
      const newBoard = prevBoard.map((row, rowIndex) =>
      rowIndex === x ? row.map((cell, cellIndex) =>
        cellIndex === y ? value : cell
      ) : row
    );
    //Convert the new changed board in a 2d grid and send it to the server
    // Make sure the string board values are sent as integers
    const backBoard = Array.from(newBoard.values()).map((row) => row.map(Number));
    axios.post('http://127.0.0.1:5000/api/update', {puzzle: backBoard})
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

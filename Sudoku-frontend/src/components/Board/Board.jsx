import React, { useState } from 'react';
import Cell from './Cell';
import './App.css'; 

const Board = () => {
  const [board, setBoard] = useState(Array(9).fill(Array(9).fill(0)));
  const [selectedCell, setSelectedCell] = useState(null);

  const handleCellChange = (x, y, value) => {
    const newBoard = board.map((row, rowIndex) => 
      rowIndex === x ? row.map((cell, cellIndex) => 
        cellIndex === y ? value : cell
      ) : row
    );
    setBoard(newBoard);
  };

  const handleCellSelect = (x, y) => {
    setSelectedCell({ x, y });
  };

  const isCellSelected = (x, y) => {
    return selectedCell && selectedCell.x === x && selectedCell.y === y;
  };

  const isSameRowOrColumnOrBox = (x, y) => {
    return (
      selectedCell &&
      (selectedCell.x === x || selectedCell.y === y || 
      Math.floor(selectedCell.x / 3) === Math.floor(x / 3) && Math.floor(selectedCell.y / 3) === Math.floor(y / 3))
    );
  };

  return (
    <div className="board">
      {board.map((row, x) => (
        <div key={x} className={`row ${x % 3 === 0 ? 'thick-top' : ''}`}>
          {row.map((value, y) => (
            <Cell 
              key={`${x}-${y}`} 
              value={value} 
              onChange={(value) => handleCellChange(x, y, value)} 
              onSelect={() => handleCellSelect(x, y)}
              selected={isCellSelected(x, y)}
              highlighted={isSameRowOrColumnOrBox(x, y)}
            />
          ))}
        </div>
      ))}
    </div>
  );
};

export default Board;

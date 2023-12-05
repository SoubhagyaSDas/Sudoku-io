import React, { useState } from 'react';
import Cell from './Cell';
import '../../App.css'; // Corrected import path for App.css

const Board = () => {
  const [board, setBoard] = useState(Array(9).fill(Array(9).fill('')));
  const [selectedCell, setSelectedCell] = useState({ x: -1, y: -1 });

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

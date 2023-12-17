import React from 'react';

const BoardSelecter = ({ onBoardChange }) => {
  return (
    <select onChange={(e) => onBoardChange(e.target.value)} className="board-selector">
      <option value="9">9x9</option>
      <option value="4">4x4</option>
    </select>
  );
};

export default BoardSelecter;

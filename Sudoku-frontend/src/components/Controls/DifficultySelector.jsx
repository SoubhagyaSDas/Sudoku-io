import React from 'react';

const DifficultySelector = ({ onDifficultyChange }) => {
  return (
    <select onChange={(e) => onDifficultyChange(e.target.value)} className="difficulty-selector">
      <option value="easy">Easy</option>
      <option value="medium">Medium</option>
      <option value="hard">Hard</option>
    </select>
  );
};

export default DifficultySelector;

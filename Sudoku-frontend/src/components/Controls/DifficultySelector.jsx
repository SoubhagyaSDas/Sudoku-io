import React from 'react';

const DifficultySelector = ({ onDifficultyChange }) => {
  return (
    <select onChange={(e) => onDifficultyChange(e.target.value)} className="difficulty-selector">
      <option value="Easy">Easy</option>
      <option value="Medium">Medium</option>
      <option value="Hard">Hard</option>
    </select>
  );
};

export default DifficultySelector;

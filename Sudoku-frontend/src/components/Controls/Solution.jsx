import React from 'react';

const GridSelector = ({ onGridSizeChange }) => {
    return (
      <select onChange={(e) => onGridSizeChange(e.target.value)} className="difficulty-selector">
        <option value="4x4">4x4</option>
        <option value="9x9">9x9</option>
      </select>
    );
  };
  
  export default GridSelector;



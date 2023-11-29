import React from 'react';

const Cell = ({ value, rowIndex, colIndex, onChange, onSelect, isHighlighted, isSelected }) => {
  const handleInputChange = e => {
    const val = e.target.value;
    if (/^[1-9]$/.test(val) || val === '') {
      onChange(rowIndex, colIndex, val);
    }
  };

  const handleClick = () => onSelect(rowIndex, colIndex);

  const cellClasses = `cell${isHighlighted ? ' highlighted' : ''}${isSelected ? ' selected' : ''}${value === '' ? ' editable' : ''}`;

  return (
    <input
      type="text"
      className={cellClasses}
      value={value}
      maxLength="1"
      onChange={handleInputChange}
      onClick={handleClick}
      readOnly={value !== ''}
    />
  );
};

export default Cell;

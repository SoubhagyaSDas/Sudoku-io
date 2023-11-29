import React from 'react';

const NumberPad = ({ onNumberSelect }) => {
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  
  return (
    <div className="number-pad">
      {numbers.map((number) => (
        <button key={number} onClick={() => onNumberSelect(number)}>
          {number}
        </button>
      ))}
    </div>
  );
};

export default NumberPad;

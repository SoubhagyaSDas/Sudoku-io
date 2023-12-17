import React from 'react';
/*start : code added by manali */
const NumberPad = ({ onSelectNumber }) => {
  return (
    <div className="number-pad">
      <div className='row col-12'>
        {numbers.map((number) => (
        <button key={number} onClick={() => onNumberSelect(number)}>
          {number}
        </button>
      ))}
</div>
    </div>
  );
};
/*end : code added by manali */
export default NumberPad;

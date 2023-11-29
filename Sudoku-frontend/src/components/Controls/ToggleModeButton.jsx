import React from 'react';

const ToggleModeButton = ({ onToggle }) => {
  return (
    <label className="toggle-mode-button">
      <input type="checkbox" onChange={onToggle} />
      <span className="slider round"></span>
    </label>
  );
};

export default ToggleModeButton;

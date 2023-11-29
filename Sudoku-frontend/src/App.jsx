import React, { useState } from 'react';
import Board from './components/Board/Board';
import DifficultySelector from './components/Controls/DifficultySelector';
import NumberPad from './components/Controls/NumberPad';
import Timer from './components/Controls/Timer';
import ToggleModeButton from './components/Controls/ToggleModeButton';
import './App.css';

function App() {
  const [darkMode, setDarkMode] = useState(true); // State to handle theme

  // Handle difficulty change
  const handleDifficultyChange = (difficulty) => {
    // Your logic here
  };

  // Handle number selection
  const handleNumberSelect = (number) => {
    // Your logic here
  };

  // Handle theme toggle
  const handleToggleMode = () => {
    setDarkMode(!darkMode); // Toggle the theme state
  };

  // Conditional class assignment based on the theme state
  const themeClass = darkMode ? 'dark-mode' : 'light-mode';

  return (
    <div className={`app ${themeClass}`}>
      <Board />
      <div className="control-panel">
        <DifficultySelector onDifficultyChange={handleDifficultyChange} />
        <NumberPad onNumberSelect={handleNumberSelect} />
        <Timer />
        <ToggleModeButton onToggle={handleToggleMode} />
        {/* Insert additional controls if necessary */}
      </div>
    </div>
  );
}

export default App;

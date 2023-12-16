import React, { useState } from 'react';
import Board from './components/Board/Board';
import DifficultySelector from './components/Controls/DifficultySelector';
import NumberPad from './components/Controls/NumberPad';
import Timer from './components/Controls/Timer';
import ToggleModeButton from './components/Controls/ToggleModeButton';
import './App.css';
import logo from "./assets/logo.png";
import hint from "./assets/hint.jpeg";
import notes from "./assets/notes.jpg";
import erase from "./assets/erase.jpeg";
import undo from "./assets/undo.jpg";


function App() {
  const [darkMode, setDarkMode] = useState(true); // State to handle theme
  const [hintRequested, setHintRequested] = useState(false); // State to track if hint is requested
  const [selectedDifficulty, setSelectedDifficulty] = useState('Easy');// Sate to track difficulty
  const [undoClicked, setUndoClicked] = useState(false);// Sate to track if erase is clicked


  // Handle difficulty change
  const handleDifficultyChange = (difficulty) => {
    // Your logic here
    setSelectedDifficulty(difficulty);
  };

  // handle hint button click
  const handleHintButtonClick = () => {
    // Set the hintRequested state to true
    setHintRequested(true);
  };

  // Handle erase button clicked
  const handleUndoClicked = () => {
    // Your logic here
    setUndoClicked(true);
  };  

  // Handle number selection
  const handleNumberSelect = (number) => {
    // Check if a cell is selected
    // if (selectedCell.x !== -1 && selectedCell.y !== -1) {
    //   // Call the function to update the selected cell with the chosen number
    //   handleCellChange(selectedCell.x, selectedCell.y, number);
    // }
  };

  // Handle theme toggle
  const handleToggleMode = () => {
    setDarkMode(!darkMode); // Toggle the theme state
  };

  

  // Conditional class assignment based on the theme state
  const themeClass = darkMode ? 'dark-mode' : 'light-mode';

  return (
    <div className={`app ${themeClass}`}>
      <div className="row">
        <div className="col-lg-2 col-md-12 col-12 menu-div">
          <div className='div-logo'>
            <img src={logo} className="logo" alt="" />
          </div>
          <div className='option-div'>
            <div>
              <a className='option-click' onClick={handleHintButtonClick}>
                <img src={hint} className='option-img'></img>
                <p className='option-text'>Hints</p>
              </a>
            </div>
            <div>
              <a className='option-click'>
                <img src={notes} className='option-img'></img>
                <p className='option-text'>Notes</p>
              </a>
            </div>
            <div>
              <a className='option-click' onClick={handleUndoClicked}>
                <img src={undo} className='option-img'></img>
                <p className='option-text'>Undo</p>
              </a>
            </div>
          </div>

        </div>
        <div className="col-lg-10 col-md-12 col-12">
          <div className="row">
            <div className="col-12">
              <DifficultySelector onDifficultyChange={handleDifficultyChange} />
              <div className='float-right mt-3 mr-3'>
                <ToggleModeButton onToggle={handleToggleMode} />
              </div>
            </div>
          </div>
          <div className="row board-div">
            <div className="col-lg-7 col-md-12 col-12">
              <div className='game-board'>
                {/* Pass Hint Click to the board */}
                <Board 
                  hintRequested={hintRequested} 
                  setHintRequested={setHintRequested} 
                  selectedDifficulty={selectedDifficulty}
                  undoClicked={undoClicked}
                  setUndoClicked={setUndoClicked}
                />
              </div>
            </div>
            <div className="col-lg-5 col-md-12 col-12 number-div">
              <div className='timer-div'>
                  <Timer />
                </div>
              <NumberPad onNumberSelect={handleNumberSelect} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

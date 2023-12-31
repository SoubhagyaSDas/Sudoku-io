import React, { useState } from 'react';
import Board from './components/Board/Board';
import DifficultySelector from './components/Controls/DifficultySelector';
import BoardSelecter from './components/Controls/BoardSelector';
import NumberPad from './components/Controls/NumberPad';
import Timer from './components/Controls/Timer';
import ToggleModeButton from './components/Controls/ToggleModeButton';
import './App.css';
import logo from "./assets/logo.png";
import hint from "./assets/hint.png";
import notes from "./assets/notes.png";
import check from "./assets/correct.jpeg";
import undo from "./assets/undo.png";
import solution from "./assets/solution.svg";

/*start : code added by manali */
function App() {
  const [darkMode, setDarkMode] = useState(true); // State to handle theme
  const [hintRequested, setHintRequested] = useState(false); // State to track if hint is requested
  const [selectedDifficulty, setSelectedDifficulty] = useState('Easy');// Sate to track difficulty
  const [selectedBoard, setSelectedBoard] = useState('9');// Sate to track board size
  const [undoClicked, setUndoClicked] = useState(false);// Sate to track if erase is clicked
  const [undoUntilCorrect, setUndoUntilCorrect] = useState(false);// Sate to track if check is clicked
  const [selectedCell, setSelectedCell] = useState({ x: -1, y: -1 });

  // Handle difficulty change
  const handleDifficultyChange = (difficulty) => {
    // Your logic here
    setSelectedDifficulty(difficulty);
  };

  // Handle difficulty change
  const handleBoardChange = (board) => {
    // Your logic here
    setSelectedBoard(board);
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

   // Handle erase button clicked
   const handleUndoUntilCorrect = () => {
    // Your logic here
    setUndoUntilCorrect(true);
  };  

  const handleNumberSelect = (number) => {
    if (selectedCell.x != null && selectedCell.y != null) {
      handleCellChange(selectedCell.x, selectedCell.y, number.toString());
    }
  };  
  

  // Handle theme toggle
  const handleToggleMode = () => {
    setDarkMode(!darkMode); // Toggle the theme state
  };

  const checkSolution = () => {

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
            <div>
              <a className='option-click' onClick={handleUndoUntilCorrect}>
                <img src={check} className='option-img'></img>
                <p className='option-text'>Undo Until Correct</p>
              </a>
            </div>
            <div>
              <a className='option-click' onClick={checkSolution}>
                <img src={solution} className='option-img'></img>
                <p className='option-text'>Solution</p>
              </a>
            </div>
          </div>

        </div>
        <div className="col-lg-10 col-md-12 col-12">
          <div className="row">
            <div className="col-12">
              <DifficultySelector onDifficultyChange={handleDifficultyChange} />
              <BoardSelecter onBoardChange={handleBoardChange} />
              <div className='float-right mt-3 mr-3'>
                <ToggleModeButton onToggle={handleToggleMode} />
              </div>
              <div className="col-lg-5 col-md-12 col-12 number-div">
              <div className='timer-div'>
                  <Timer />
              </div>
            </div>
            </div>
          </div>
          <div className="row board-div">
            <div className="col-lg-12 col-md-12 col-12">
              <div className='game-board'>
                {/* Pass Hint Click to the board */}
                <Board 
                  selectedDifficulty={selectedDifficulty}
                  selectedBoard={selectedBoard}
                  hintRequested={hintRequested} 
                  setHintRequested={setHintRequested} 
                  undoClicked={undoClicked}
                  setUndoClicked={setUndoClicked}
                  undoUntilCorrect={undoUntilCorrect}
                  setUndoUntilCorrect={setUndoUntilCorrect}
                />
              </div>
            </div>
            <div className="col-lg-7 col-md-12 col-12 number-div">
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
/*end : code added by manali */
export default App;

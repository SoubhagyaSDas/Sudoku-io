import React from 'react';
import './App.css';

function App() {
  // This function could be expanded to handle game logic
  const startGame = () => {
    console.log('Game started!');
  };

  return (
    <div className="App">
      <h1>Sudoku Game for 60th St</h1>
      <div className="game-board">
        {/* Placeholder for the Sudoku board */}
        <p>Happy Diwali</p>
      </div>
      <div className="game-controls">
        <button onClick={startGame}>Start Game</button>
        {/* Add more buttons as needed */}
      </div>
    </div>
  );
}

export default App;

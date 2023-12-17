# Sudoku Web Application Frontend Documentation

## Overview

This document outlines the structure and styling of the frontend components for the Sudoku web application. The application provides a user-friendly interface for playing Sudoku, offering various board sizes and difficulty levels.

## Components

The frontend is composed of several React components, each serving a distinct purpose:

### `App`

The central component that orchestrates the Sudoku game. It maintains the application's state, including theme, difficulty level, and board size.

- **State Variables:**
  - `darkMode`: Boolean indicating whether the dark theme is enabled.
  - `hintRequested`: Boolean indicating if a hint has been requested.
  - `selectedDifficulty`: String representing the current difficulty level.
  - `boardSize`: Number indicating the size of the Sudoku board (4x4 or 9x9).

- **Handlers:**
  - `handleDifficultyChange`: Updates the difficulty level.
  - `handleNumberSelect`: Handles number selection for the Sudoku board.
  - `handleToggleMode`: Toggles between dark and light themes.
  - `handleHintButtonClick`: Triggers a hint request.
  - `handleBoardSizeChange`: Updates the board size.

### `Board`

Renders the Sudoku board based on the selected size and difficulty. Interacts with `Cell` components to display individual Sudoku cells.

### `DifficultySelector`

A dropdown component allowing the user to select the difficulty level of the game.

### `Grid`

A dropdown component allowing the user to select the size of the Sudoku board (4x4 or 9x9).

### `NumberPad`

Displays a number pad for the user to input numbers into the Sudoku board.

### `Timer`

Keeps track of the time spent on the current game.

### `ToggleModeButton`

Allows users to switch between dark and light themes.

## Styling

Styles are defined across several CSS files:

### `App.css`

Defines the global styles for the application, including the layout, typography, and color themes for dark and light modes.

### `controls.css`

Contains styles for all control elements such as buttons, selectors, and the number pad. It ensures that the controls are visually consistent and aligned properly.

- **`.control-panel`:** Ensures that the difficulty selector and grid size dropdown are displayed in a row with appropriate spacing.
- **`.grid-selector`:** Styles the grid size dropdown to look identical to the difficulty selector and positions it 10px to the right.
- **`.toggle-mode`:** Styles the theme toggle button.

## Interaction Flow

The `App` component renders a control panel at the top, allowing users to select the difficulty and board size. Below the control panel, the main game board is displayed alongside a number pad. The board updates in real-time based on user interactions with the control panel.

## Responsive Design

The application is designed to be responsive, adapting to various screen sizes and orientations. Flexbox is used extensively in the layout to ensure components are aligned and distributed evenly.

---

This documentation provides an overview of the frontend structure and should be updated as the application evolves. For more detailed information on individual components or specific implementation details, refer to the source code and inline comments.

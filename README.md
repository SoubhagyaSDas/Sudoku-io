# Project Title
Sudoku-web-app

## Description
A brief description of your Sudoku game project.

## Installation and Setup
Instructions on how to clone, install dependencies, and run the project.

## Usage
How to use the application, including any available commands or interfaces.

## Progress and Achievements
- Initial setup with React using create-react-app.
- Development of a basic React structure for the game.
- Integration of React with custom HTML/CSS.
- Outline of future steps and features.
- Backend: Representation & algorithms 

Structure of the game:
sudoku-game/
│
├── Frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar/
│   │   │   │   ├── Navbar.js
│   │   │   │   ├── Navbar.css
│   │   │   ├── GameBoard/
│   │   │   │   ├── GameBoard.js
│   │   │   │   ├── GameBoard.css
│   │   │   ├── Footer/
│   │   │       ├── Footer.js
│   │   │       ├── Footer.css
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │
│   ├── public/
│   │   ├── index.html
│   │   └── ... (other public assets)
│   │
│   ├── package.json
│   └── ... (other config files like .gitignore, README.md)
│
└── Backend/
    └── (To be structured later)
## Project Structure

### Backend

The `Sudoku-backend` folder contains all the backend logic for our Sudoku Web App. This includes:

- **Backend Logic:** The core functionality of the Sudoku game, including communication between the backend and the database.
  
- **API Documentation:** Detailed documentation for the API endpoints used in the backend.

- **Testing Files:** All the testing files for the backend are located in the `Sudoku-backend` folder.

### Frontend

The frontend of our web app is organized into folders containing JSX files, inside `Sudoku-frontend`  These files collectively form the user interface and functionality of the Sudoku Web App.

### Contributions

Details about individual contributions can be found in the main branch of this repository in the file called: Contributions. Please also refer to the commit history for a comprehensive overview of the contributions made by each team member.

### Documentation

- **Class Diagram:** The class diagram for our project is available in the Wiki section of this repository.
  
- **Storyboards:** You can find the storyboards illustrating the user experience in the Wiki section as well.

- **Use Case Diagram:** You can find the use case diagram illustrating the user's possible actions in the Wiki section as well.

- **Project Plan:** Initial Trello Board can also be found in the Wiki section. 

## Running the App

This Sudoku Web App is built using Flask. To run the application, ensure you have Flask installed. You can install it using the following command:

```bash
pip install Flask

After installing Flask, navigate to the Sudoku-backend folder and run the following commands to start the Flask app:

```bash
cd Sudoku-backend
python server.py

The frontend of our web app is built using npm. To run the frontend development server, navigate to the Sudoku-frontend folder and run the following commands:
```bash
cd Sudoku-frontend
npm install  # Install dependencies (required only once)
npm run dev   # Start the development server


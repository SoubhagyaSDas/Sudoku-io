# Sudoku Web App

Welcome to our Sudoku Web App repository! In this repository, you will find all the necessary files and information related to our Sudoku Web App project.
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

### Documentation (all found in the Wiki section)

- **Class Diagram:** The representations of all the classes and their attributes and methods for our project.
  
- **Storyboards:** The design we intially came up with and the design we ended up going with to illustrate the user experience.

- **Use Case Diagram:** All the user's possible actions in our Sudoku application.

- **Project Plan:** Initial Trello Board reflecting our project goals and timeline.

- **Testing Plan:** The plan to "play" through a game to test the backend functionality.

- **Testing Results:** Scripts and log files of backend testing.

## Running the App

This Sudoku Web App is built using Flask. To run the application, ensure you have Flask installed. You can install it using the following command:

```bash
pip install Flask
pip install Flask_cors
pip install firestore_admin

After installing Flask, navigate to the Sudoku-backend folder and run the following commands to start the Flask app:

```bash
cd Sudoku-backend
python server.py

The frontend of our web app is built using npm. To run the frontend development server, navigate to the Sudoku-frontend folder and run the following commands:
```bash
cd Sudoku-frontend
npm install  # Install dependencies (required only once)
npm run dev   # Start the development server


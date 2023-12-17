#API documentation for Backend to DB communciation by Nashrah

## Overview
This API allows you to interact with a Sudoku puzzle application that uses Firebase Firestore for puzzle storage and retrieval.

## Base URL
`https://your-api-base-url.com`

## Endpoints

### 1. Save Sudoku Puzzle to Database
- **Endpoint:** `/save`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "sudoku": {
      "boardSize": 9,
      "difficulty": "medium",
      "grid": [
        // 2D array representing the user's puzzle
      ]
    },
    "sudokuSol": {
      "boardSize": 9,
      "difficulty": "medium",
      "grid": [
        // 2D array representing the solved puzzle
      ]
    }
  }
### 2. Load Sudoku Puzzle from Database
- **Endpoint:** `/load/{puzzleId}`
- **Method:** `GET`
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "difficulty": "medium",
      "size": 9,
      "board": [
        // 2D array representing the user's puzzle
      ],
      "solvedBoard": [
        // 2D array representing the solved puzzle
      ]
    }
    ```
  - Status Code: `404 Not Found`
    - Body:
      ```json
      {
        "message": "Puzzle not found"
      }
### 3. Update Sudoku Puzzle
- **Endpoint:** `/update`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "newBoard": [
      // 2D array representing the updated puzzle board
    ]
  }
- Status Code: '200 OK'
-Body:
 Json: {
  "message": "Puzzle updated successfully"
}
Example Request: 
POST /update
Content-Type: application/json

{
  "newBoard": [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
}
Example Response:
{
  "message": "Puzzle updated successfully"
}
### 4. Load Sudoku Puzzle by Difficulty
- **Endpoint:** `/load/{difficulty}`
- **Method:** `GET`
- **Response:**
  - Status Code: `200 OK`
  - Body:
    ```json
    {
      "difficulty": "medium",
      "size": 9,
      "board": [
        // 2D array representing the user's puzzle
      ],
      "solvedBoard": [
        // 2D array representing the solved puzzle
      ]
    }
    ```
  - Status Code: `404 Not Found`
    - Body:
      ```json
      {
        "message": "Puzzle not found for the given difficulty"
      }
      


from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS #pip install flask_cors
from representations import GameEngine, Cell
from backendtodb import load_from_database, save_to_database, update

app = Flask(__name__)
CORS(app, supports_credentials=True)
sudoku = GameEngine()

@app.route('/api/get_puzzle/<puzzle_id>', methods=['POST'])
def generate_sudoku():
    save_to_database(sudoku.puzzle, sudoku.solvedPuzzle)

@app.route('/api/get_puzzle/<puzzle_id>', methods=['GET'])
def get_puzzle(puzzle_id):
    # load the puzzles into the user board and another used to verify
    load_from_database(puzzle_id, sudoku.puzzle, sudoku.solvedPuzzle)
    # Converting puzzle information to json
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = sudoku.puzzle.grid[i][j].GetEntry()

    # Converting puzzle information to json
    solvedBoard = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            solvedBoard[i][j] = sudoku.solvedPuzzle.grid[i][j].GetEntry()
        
    return jsonify({'puzzle': board,
                    'solvedPuzzle': solvedBoard})

@app.route('/api/hint', methods=['GET'])
def getHint():
    sudoku.GetRandomHint()
    updateBoard()
    return get_puzzle(sudoku.puzzle.GetBoardID())

@app.route('/api/update', methods =['POST'])
def updateBoard():
    # Fetch the json of the updated board
    data = request.get_json()
    new_board = data.get('puzzle')
    # Pass new grid and game engine puzzle to the backenddb function
    update(new_board, sudoku.puzzle)
    return jsonify({'Message': 'Works'})

if __name__ == '__main__':
    app.run(debug=True)
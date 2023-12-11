from flask import Flask, request, jsonify
from flask_cors import CORS
from representations import GameEngine
from backendtodb import load_from_database, save_to_database, update

app = Flask(__name__)
CORS(app)
sudoku = GameEngine()


@app.route('/api/get_puzzle/<puzzle_id>', methods=['POST'])
def generate_sudoku():
    save_to_database(sudoku.puzzle)

@app.route('/api/get_puzzle/<puzzle_id>', methods=['GET'])
def get_puzzle(puzzle_id):
    load_from_database(puzzle_id, sudoku.puzzle)
    # Converting puzzle information to json
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = sudoku.puzzle.grid[i][j].GetEntry()
    return jsonify({'puzzle': board})

@app.route('/api/update', methods =['POST'])
def updateBoard():
    # Fetch the json of the updated board
    data = request.get_json()
    new_board = data.get('puzzle')
    # Pass new grid and game engine puzzle to the backenddb function
    update(new_board, sudoku.puzzle)
    return({'Message', 'Works'})

if __name__ == '__main__':
    app.run(debug=True)
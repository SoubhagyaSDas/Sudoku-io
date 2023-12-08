from flask import Flask, request, jsonify
from flask_cors import CORS
from representations import Cell, Puzzle
from backendtodb import load_from_database, save_to_database

app = Flask(__name__)
CORS(app)
sudoku = Puzzle()

@app.route('/api/get_puzzle/<puzzle_id>', methods=['POST'])
def generate_sudoku():
    save_to_database(sudoku)

@app.route('/api/get_puzzle/<puzzle_id>', methods=['GET'])
def get_puzzle(puzzle_id):
    load_from_database(puzzle_id, sudoku)
    # Converting puzzle information to json
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = sudoku.grid[i][j].GetEntry()
    return jsonify({'puzzle': board})


# @app.route('/api/update', methods =['POST'])
# def updateBoard():
#     updateData = request.get_json()
#     puzzle = updateData['puzzle']

if __name__ == '__main__':
    app.run(debug=True)
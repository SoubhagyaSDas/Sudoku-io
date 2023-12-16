from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS, cross_origin #pip install flask_cors
from representations import GameEngine, Cell
from backendtodb import load_from_database, save_to_database, update, load

app = Flask(__name__)
CORS(app, supports_credentials=True)
sudoku = GameEngine()

# entry = [[0,0,3,6,0,0,0,0,0], [9,0,0,8,0,0,2,0,7], [0,0,0,0,0,0,0,0,0], [0,4,0,1,5,0,8,3,0], [0,7,0,0,0,4,0,0,0], [8,2,0,0,0,0,0,0,0], [0,9,0,0,0,5,3,0,8], [5,0,0,7,6,0,4,0,0], [0,0,0,0,0,0,5,6,0]]

# sudoku.puzzle.SetBoardSize(9)
# sudoku.puzzle.SetDifficulty('Hard')
# sudoku.puzzle.grid = [[Cell() for _ in range(9)] for _ in range(9)]
# sudoku.solvedPuzzle.grid = [[Cell() for _ in range(9)] for _ in range(9)]
# for i in range(9):
#     for j in range(9):
#         sudoku.puzzle.grid[i][j].SetEntry(entry[i][j])

@app.route('/api/get_puzzle/<puzzle_id>', methods=['POST'])
@cross_origin()
def generate_sudoku():
    save_to_database(sudoku.puzzle, sudoku.solvedPuzzle)

#By Nashrah
@app.route('/api/get_puzzle/<puzzle_id>', methods=['GET'])
@cross_origin()
def get_puzzle(puzzle_id):
    # load the puzzles into the user board and another used to verify
    load_from_database(puzzle_id, sudoku.puzzle, sudoku.solvedPuzzle)

    # Converting puzzle information to JSON
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = sudoku.puzzle.grid[i][j].GetEntry()
            mutable = sudoku.puzzle.grid[i][j].IsMutable()
            row.append({'entry': entry, 'mutable': mutable})
        board.append(row)

    # Converting puzzle information to JSON
    solvedBoard = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            solvedBoard[i][j] = sudoku.solvedPuzzle.grid[i][j].GetEntry()

    return jsonify({'puzzle': board,
                    'solvedPuzzle': solvedBoard})


@app.route('/api/hint', methods=['GET'])
@cross_origin()
def getHint():
    sudoku.GetRandomHint()
    updateBoard()
    return get_puzzle(sudoku.puzzle.GetBoardID())
    
#Changed update route by Nashrah
# Update route
@app.route('/api/update', methods=['POST'])
@cross_origin()
def updateBoard():
    data = request.get_json()
    new_board = data.get('puzzle')

    if 'erase' in str(new_board):
        # Handle erase logic (set the corresponding cell to 0 in the database)
        for i in range(len(new_board)):
            for j in range(len(new_board[i])):
                if sudoku.puzzle.grid[i][j].IsMutable():
                    sudoku.puzzle.grid[i][j].SetEntry(0)
        save_to_database(sudoku.puzzle, sudoku.solvedPuzzle)
    else:
        # Handle regular numeric values
        update(new_board, sudoku.puzzle)

    return jsonify({'Message': 'Board updated successfully'})


# Load puzzle by difficulty
@app.route('/api/load_puzzle/<difficulty>', methods=['GET'])
@cross_origin()
def load_puzzle(difficulty):
    # load the puzzles into the user board and another used to verify
    load(difficulty, sudoku.puzzle, sudoku.solvedPuzzle)
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

if __name__ == '__main__':
    app.run(debug=True)

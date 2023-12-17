from flask import Flask, request, jsonify #pip install flask
from flask_cors import CORS, cross_origin #pip install flask_cors
from representations import GameEngine, HxEntry, Cell, Puzzle
from backendtodb import load_from_database, save_to_database, update, load

app = Flask(__name__)
CORS(app, supports_credentials=True, origins="http://127.0.0.1:5173/")
sudoku = GameEngine()

def convertGridToBoard(board: list, puzzle: Puzzle()):
    size = sudoku.puzzle.GetBoardSize()
    for row in range(size):
        board.append([puzzle.grid[row][col].GetEntry() for col in range(size)])
    return board

@app.route('/api/get_puzzle/<puzzle_id>/', methods=['POST'])
@cross_origin()
def generate_sudoku():
    save_to_database(sudoku.puzzle, sudoku.solvedPuzzle)

#By Nashrah
@app.route('/api/get_puzzle/<puzzle_id>/', methods=['GET'])
@cross_origin()
def get_puzzle(puzzle_id):
    # load the puzzles into the user board and another used to verify
    load_from_database(puzzle_id, sudoku.puzzle, sudoku.solvedPuzzle)
    # Converting puzzle information to json
    board = convertGridToBoard([], sudoku.puzzle)

    # Converting puzzle information to json
    solvedBoard = convertGridToBoard([], sudoku.solvedPuzzle)
        
    return jsonify({'puzzle': board,
                    'solvedPuzzle': solvedBoard})

@app.route('/api/hint/', methods=['GET'])
@cross_origin()
def getHint():
    hint = sudoku.GetRandomHint()
    board = convertGridToBoard([], sudoku.puzzle)
    board[hint[0]][hint[1]] = hint[2]

    update(board, sudoku.puzzle)
    return jsonify({'puzzle': board})

@app.route('/api/update/', methods =['POST'])
@cross_origin()
def updateBoard():
    # Fetch the json of the updated board and the newcell and rows
    data = request.get_json()
    board = data.get('puzzle')
    new = data.get('new')
    row, col = data.get('row'), data.get('col')
    
    oldCell, newCell = Cell(), Cell()
    # Oldcell is set to cell before update
    oldCell.SetEntry(sudoku.puzzle.grid[row][col].GetEntry(), row, col)
    # Newcell is set to value sent from frontend
    newCell.SetEntry(new, row, col)
    # update the puzzle itself
    
    correct = sudoku.algo.IsValidMove(sudoku.puzzle, row, col, newCell.GetEntry())# check correctness of move
    # Store the newcell value in gameengine puzzle
    sudoku.puzzle.grid[row][col].SetEntry(board[row][col])
    entry = HxEntry()
    entry.CreateEntry(oldCell, newCell, correct) # Create a new history entry and put it in the stack
    sudoku.history.AddToHistory(entry)
    # print(board)
    # Pass new grid and game engine puzzle to the backenddb function
    update(board, sudoku.puzzle)
    return jsonify({'Message': 'Board updated successfully'})

@app.route('/api/undo/', methods =['GET'])
@cross_origin()
def undoMove():
    # Get the last entry from history
    move = sudoku.Undo()
    if move is not None:
        #Get board information
        board = convertGridToBoard([], sudoku.puzzle)
        row,col = move.oldCell.row, move.oldCell.col
        # Change the puzzle and board of the move to oldmove
        board[row][col] = move.oldCell.GetEntry()
        sudoku.puzzle.grid[row][col].SetEntry(board[row][col])
        update(board, sudoku.puzzle)
        return jsonify({'puzzle': board})

@app.route('/api/undoUntilCorrect/', methods =['GET'])
@cross_origin()
def UndoUntilCorrect():
    # Get the board
    board = convertGridToBoard([], sudoku.puzzle)
    # Get all the wrong made moves
    movesToUndo = sudoku.UndoUntilCorrect()

    # If there are any wrong moves
    if movesToUndo:
        for i in range(len(movesToUndo)):
            move = movesToUndo[i]
            # print(move.isCorrect)
            row,col = move.oldCell.row, move.oldCell.col
            board[row][col] = move.oldCell.GetEntry()
            sudoku.puzzle.grid[row][col].SetEntry(board[row][col])
        update(board, sudoku.puzzle)
    return jsonify({'puzzle': board})
            
# Load puzzle by difficulty
@app.route('/api/load_puzzle/<difficulty>/', methods=['GET'])
@cross_origin()
def load_puzzle(difficulty):

    # load the puzzles into the user board and another used to verify
    load(difficulty, sudoku.puzzle, sudoku.solvedPuzzle)
    # Converting puzzle information to json
    board = convertGridToBoard([], sudoku.puzzle)
    # Converting puzzle information to json
    solvedBoard = convertGridToBoard([], sudoku.solvedPuzzle)
        
    return jsonify({'puzzle': board,
                    'solvedPuzzle': solvedBoard})

# Load puzzle by difficulty and size
@app.route('/api/load_board', methods=['GET'])
@cross_origin()
def load_board():
    difficulty = request.args.get('difficulty', type=str, default='Easy')
    size = request.args.get('size', type=int, default=9)
    # load the puzzles into the user board and another used to verify
    load(difficulty, size, sudoku.puzzle, sudoku.solvedPuzzle)
    # Converting puzzle information to json
    board = convertGridToBoard([], sudoku.puzzle)
    # Converting puzzle information to json
    solvedBoard = convertGridToBoard([], sudoku.solvedPuzzle)
        
    return jsonify({'puzzle': board,
                    'solvedPuzzle': solvedBoard})

if __name__ == '__main__':
    app.run(debug=True)
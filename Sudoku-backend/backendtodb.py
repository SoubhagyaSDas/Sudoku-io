import json  # Used to serialize/deserialize puzzle data
import firebase_admin #pip install firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from representations import Cell, Puzzle, Algorithms

# credentials to verify firestore link
cred = credentials.Certificate('./sudoku-io-firebase-adminsdk-gsy8b-2677c25397.json')
fireApp = firebase_admin.initialize_app(cred)
db = firestore.client() #Open firebase db
algo = Algorithms()

#Pass sudoku object to store to database
def save_to_database(sudoku: Puzzle(), sudokuSol: Puzzle()):
    # Reference to collection of puzzles
    puzzle_ref = db.collection('puzzles')

    # Copy the user board and post in the solution grid
    for i in range(sudoku.GetBoardSize()):
        for j in range(sudoku.GetBoardSize()):
            sudokuSol.grid[i][j].SetEntry(sudoku.grid[i][j].GetEntry())
    #solve the board
    algo.SolvePuzzle(sudokuSol)
    # Empty board to convert cell lists to 2d nymber list
    board = [[0 for _ in range(sudoku.GetBoardSize())] for _ in range(sudoku.GetBoardSize())]
    for i in range(sudoku.GetBoardSize()):
        for j in range(sudoku.GetBoardSize()):
            board[i][j] = sudoku.grid[i][j].GetEntry()
    # Create an empty board to convert list of Cells to firestore format
    firestore_board = {}
    for i, row in enumerate(board, start=1):
        firestore_board[f'row{i}'] = {f'col{j}': value for j, value in enumerate(row, start=1)}

    #store the solution to db
    board = [[0 for _ in range(sudoku.GetBoardSize())] for _ in range(sudoku.GetBoardSize())]
    for i in range(sudoku.GetBoardSize()):
        for j in range(sudoku.GetBoardSize()):
            board[i][j] = sudokuSol.grid[i][j].GetEntry()

    Solfirestore_board = {}
    for i, row in enumerate(board, start=1):
        Solfirestore_board[f'row{i}'] = {f'col{j}': value for j, value in enumerate(row, start=1)}

    doc_id = puzzle_ref.document("count") #Read from collection of puzzle count
    get_count = doc_id.get(field_paths={"puzzleCount"}).to_dict()#Store puzzle count
    count = get_count.get("puzzleCount") + 1 #Add 1 to puzzle count
    doc_id.update({'puzzleCount': count}) #Update firestore count data

    # Puzzle information to be sent to firestore
    data = {
        "difficulty": sudoku.GetDifficulty(),
        "size": sudoku.GetBoardSize(),
        "board": firestore_board,
        "solvedBoard": Solfirestore_board
    }
    # saving to database
    puzzle_ref.document(str(count)).set(data)

#Pass puzzle_id and sudoku object to function
def load_from_database(puzzle_id, sudoku: Puzzle(), sudokuSol: Puzzle()):
    boardDocs = db.collection("puzzles")#Connects to puzzle storage doc
    doc_ref = boardDocs.document(str(puzzle_id)).get()# Reference to the specific puzzle document

    # if puzzzle with the id exist
    if doc_ref.exists:
        puzzle_data = doc_ref.to_dict() #Store puzzle data
        # Board size
        size = puzzle_data['size']
        sudoku.SetDifficulty(puzzle_data['difficulty'])#Set puzzle difficulty to stored
        sudoku.SetBoardID(puzzle_id)
        sudoku.SetBoardSize(size)#Set puzzle size to stored
        board_data = puzzle_data['board'] #Set board  to stored
        solved_data = puzzle_data['solvedBoard'] #Store the solved board

        #convert the firestore board to a 2D List of the numbers
        board = [[board_data[f'row{i}'][f'col{j}'] for j in range(1, size+1)] for i in range(1, size+1)]
        #Set the grid to the cells
        sudoku.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        # Fill the cells with number
        for i in range(size):
            for j in range(size):
                sudoku.grid[i][j].SetEntry(board[i][j])

        # Store the
        solved = [[solved_data[f'row{i}'][f'col{j}'] for j in range(1, size+1)] for i in range(1, size+1)]
        #Set the grid to the cells
        sudokuSol.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        # Fill the cells with number
        for i in range(size):
            for j in range(size):
                sudokuSol.grid[i][j].SetEntry(solved[i][j])
    else:
        print("Does not work")

#By Nashrah
def update(new_board: list, sudoku: Puzzle()):
    #Connects to puzzle storage doc
    puzzle_ref = db.collection('puzzles')

    # Convert updated board to firestore format
    firestore_board = {}
    for i, row in enumerate(new_board, start=1):
        firestore_board[f'row{i}'] = {f'col{j}': value for j, value in enumerate(row, start=1)}
    # Store the updated board to firestore
    puzzle_ref.document(str(sudoku.GetBoardID())).update({'board': firestore_board})

def load(difficulty, sudoku: Puzzle(), sudokuSol: Puzzle()):
    # Get total count
    doc_id = db.collection('puzzles').document("count") #Read from collection of puzzle count
    get_count = doc_id.get(field_paths={"puzzleCount"}).to_dict()#Store puzzle count
    count = get_count.get("puzzleCount")

    boardDocs = db.collection("puzzles")#Connects to puzzle storage doc
    # Loop through the database
    for boardID in range(1,count):
        doc_ref = boardDocs.document(str(boardID)).get()# Reference to the specific puzzle document
        # If puzzle exists
        if doc_ref.exists:
            puzzle_data = doc_ref.to_dict() #Store puzzle data
            # If the puzzle matches the chosen difficulty retrieve it
            if puzzle_data['size'] == 9 and puzzle_data['difficulty'] == difficulty:
                size = puzzle_data['size']
                sudoku.SetDifficulty(puzzle_data['difficulty'])#Set puzzle difficulty to stored
                sudoku.SetBoardID(boardID)
                sudoku.SetBoardSize(size)#Set puzzle size to stored
                board_data = puzzle_data['board'] #Set board  to stored
                solved_data = puzzle_data['solvedBoard'] #Store the solved board

                #convert the firestore board to a 2D List of the numbers
                board = [[board_data[f'row{i}'][f'col{j}'] for j in range(1, 10)] for i in range(1, 10)]
                #Set the grid to the cells
                sudoku.grid = [[Cell() for _ in range(size)] for _ in range(size)]
                # Fill the cells with number
                for i in range(size):
                    for j in range(size):
                        sudoku.grid[i][j].SetEntry(board[i][j])

                # Store the
                solved = [[solved_data[f'row{i}'][f'col{j}'] for j in range(1, 10)] for i in range(1, 10)]
                #Set the grid to the cells
                sudokuSol.grid = [[Cell() for _ in range(size)] for _ in range(size)]
                # Fill the cells with number
                for i in range(size):
                    for j in range(size):
                        sudokuSol.grid[i][j].SetEntry(solved[i][j])
                break
        else:
            print("Does not work")

def load(difficulty, size, sudoku: Puzzle(), sudokuSol: Puzzle()):
    # Get total count
    doc_id = db.collection('puzzles').document("count") #Read from collection of puzzle count
    get_count = doc_id.get(field_paths={"puzzleCount"}).to_dict()#Store puzzle count
    count = get_count.get("puzzleCount")

    boardDocs = db.collection("puzzles")#Connects to puzzle storage doc
    # Loop through the database
    for boardID in range(1,count):
        doc_ref = boardDocs.document(str(boardID)).get()# Reference to the specific puzzle document
        # If puzzle exists
        if doc_ref.exists:
            puzzle_data = doc_ref.to_dict() #Store puzzle data
            # If the puzzle matches the chosen difficulty retrieve it
            if puzzle_data['size'] == size and puzzle_data['difficulty'] == difficulty:
                boardSize = puzzle_data['size']
                sudoku.SetDifficulty(puzzle_data['difficulty'])#Set puzzle difficulty to stored
                sudoku.SetBoardID(boardID)
                sudoku.SetBoardSize(boardSize)#Set puzzle size to stored
                board_data = puzzle_data['board'] #Set board  to stored
                solved_data = puzzle_data['solvedBoard'] #Store the solved board

                #convert the firestore board to a 2D List of the numbers
                board = [[board_data[f'row{i}'][f'col{j}'] for j in range(1, boardSize+1)] for i in range(1, boardSize+1)]
                #Set the grid to the cells
                sudoku.grid = [[Cell() for _ in range(boardSize)] for _ in range(boardSize)]
                # Fill the cells with number
                for i in range(boardSize):
                    for j in range(boardSize):
                        sudoku.grid[i][j].SetEntry(board[i][j])

                # Store the
                solved = [[solved_data[f'row{i}'][f'col{j}'] for j in range(1, boardSize+1)] for i in range(1, boardSize+1)]
                #Set the grid to the cells
                sudokuSol.grid = [[Cell() for _ in range(boardSize)] for _ in range(boardSize)]
                # Fill the cells with number
                for i in range(boardSize):
                    for j in range(boardSize):
                        sudokuSol.grid[i][j].SetEntry(solved[i][j])
                break
        else:
            print("Does not work")
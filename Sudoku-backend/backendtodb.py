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
def save_to_database(sudoku: Puzzle()):
    # Reference to collection of puzzles
    puzzle_ref = db.collection('puzzles')


    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            board[i][j] = sudoku.grid[i][j].GetEntry()
    # Create an empty board to convert list of Cells to firestore format
    firestore_board = {}
    for i, row in enumerate(board, start=1):
        firestore_board[f'row{i}'] = {f'col{j}': value for j, value in enumerate(row, start=1)}

    doc_id = puzzle_ref.document("count") #Read from collection of puzzle count
    get_count = doc_id.get(field_paths={"puzzleCount"}).to_dict()#Store puzzle count
    count = get_count.get("puzzleCount") + 1 #Add 1 to puzzle count
    doc_id.update({'puzzleCount': count}) #Update firestore count data

    # Puzzle information to be sent to firestore
    data = {
        "difficulty": sudoku.GetDifficulty(),
        "size": sudoku.GetBoardSize(),
        "board": firestore_board
    }
    # saving to database
    puzzle_ref.document(str(count)).set(data)

#Pass puzzle_id and sudoku object to function
def load_from_database(puzzle_id, sudoku: Puzzle()):
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

        #convert the firestore board to a 2D List of the numbers
        board = [[board_data[f'row{i}'][f'col{j}'] for j in range(1, 10)] for i in range(1, 10)]
        #Set the grid to the cells
        sudoku.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        # Fill the cells with number
        for i in range(size):
            for j in range(size):
                sudoku.grid[i][j].SetEntry(board[i][j])
    else:
        print("Does not work")

def update(new_board: list, sudoku: Puzzle()):
    #Connects to puzzle storage doc
    puzzle_ref = db.collection('puzzles')

    # Convert updated  board to firestore format
    firestore_board = {}
    for i, row in enumerate(new_board, start=1):
        firestore_board[f'row{i}'] = {f'col{j}': value for j, value in enumerate(row, start=1)}
    # Store the updated board to firestore
    puzzle_ref.document(str(sudoku.GetBoardID())).update({'board': firestore_board})
    # ... (other methods remain unchanged from the representations.py file)
import sqlite3
import json

class HxEntry:
    def __init__(self):
        self.oldCell = Cell
        self.newCell = Cell
        self.isCorrect = True
        self.puzzle = Puzzle

    def save_to_database(self):
        # Serialize hxentry data to JSON
        serialized_data = json.dumps({
            "OldCell": {"Row": self.oldCell.GetRow(), "Col": self.oldCell.GetCol()},
            "NewCell": {"Row": self.newCell.GetRow(), "Col": self.newCell.GetCol()},
            "IsCorrect": self.isCorrect,
            "PuzzleID": self.puzzle.get_puzzle_id()
        })

        # Save hxentry data to the database
        connection = sqlite3.connect("sudoku.db")
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO "HxEntries" ("Data") VALUES (?)
        ''', (serialized_data,))
        connection.commit()
        connection.close()

    # ... (other methods remain unchanged)

class History:
    def __init__(self):
        self.history = []

    def save_to_database(self):
        # Save history data to the database
        connection = sqlite3.connect("sudoku.db")
        cursor = connection.cursor()
        
        for entry in self.history:
            entry.save_to_database()
        
        connection.commit()
        connection.close()

    # ... (other methods remain unchanged)

class Algorithms:
    def __init__(self) -> None:
        self.rand = []
    # ... (other methods remain unchanged)

class GameEngine:
    def __init__(self):
        self.puzzle = Puzzle()
        self.currentValue = 0
        self.history = History()
        self.algo = Algorithms()

    def save_to_database(self):
        # Save game engine data to the database
        connection = sqlite3.connect("sudoku.db")
        cursor = connection.cursor()
        
        self.puzzle.save_to_database()
        self.history.save_to_database()
        
        connection.commit()
        connection.close()

    # ... (other methods remain unchanged)


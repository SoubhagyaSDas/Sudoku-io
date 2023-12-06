import sqlite3
import json  # Used to serialize/deserialize puzzle data

class Puzzle:
    def __init__(self):
        self.difficulty = "Easy"
        self.size = 9
        self.grid = [[]]

        # Connect to the SQLite database
        self.connection = sqlite3.connect("sudoku.db")
        self.cursor = self.connection.cursor()

        # Initialize the database schema
        self._init_database()

    def _init_database(self):
        # Create a table to store puzzle data
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS "Puzzles" (
                "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
                "Difficulty" TEXT,
                "Size" INTEGER,
                "Grid" TEXT
            )
        ''')
        self.connection.commit()

    def save_to_database(self):
        # Serialize puzzle data to JSON
        serialized_grid = json.dumps([[cell.GetEntry() for cell in row] for row in self.grid])

        # Save puzzle data to the database
        self.cursor.execute('''
            INSERT INTO "Puzzles" ("Difficulty", "Size", "Grid") VALUES (?, ?, ?)
        ''', (self.difficulty, self.size, serialized_grid))
        self.connection.commit()

    def load_from_database(self, puzzle_id):
        # Load puzzle data from the database
        self.cursor.execute('''
            SELECT "Difficulty", "Size", "Grid" FROM "Puzzles" WHERE "ID" = ?
        ''', (puzzle_id,))
        row = self.cursor.fetchone()

        if row:
            self.difficulty, self.size, serialized_grid = row

            # Deserialize puzzle data from JSON
            self.grid = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
            deserialized_grid = json.loads(serialized_grid)
            
            for i in range(self.size):
                for j in range(self.size):
                    self.grid[i][j].SetEntry(deserialized_grid[i][j])

    def close_connection(self):
        if self.connection:
            self.connection.close()
            
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


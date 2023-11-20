from flask import Flask, request, jsonify
import sqlite3
from typing import List

app = Flask(__name__)

# Define the Puzzle and Cell classes
class Cell:
    def __init__(self, value: int):
        self.value = value

class Puzzle:
    def __init__(self, grid: List[List[int]]):
        self.grid = [[Cell(value) for value in row] for row in grid]

# Connect to the SQLite database (create a new one if it doesn't exist)
conn = sqlite3.connect('sudoku.db', check_same_thread=False)
cursor = conn.cursor()

# Create the Puzzle table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Puzzle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grid TEXT NOT NULL
    )
''')
conn.commit()

def is_valid_move(puzzle: Puzzle, row: int, col: int, num: int) -> bool:
    # Check if placing the number at the given position is a valid move
    for i in range(9):
        if puzzle.grid[row][i].value == num or puzzle.grid[i][col].value == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if puzzle.grid[start_row + i][start_col + j].value == num:
                return False

    return True

def solve_puzzle(puzzle: Puzzle) -> bool:
    # Recursive backtracking algorithm to solve the Sudoku puzzle
    for row in range(9):
        for col in range(9):
            if puzzle.grid[row][col].value == 0:
                for num in range(1, 10):
                    if is_valid_move(puzzle, row, col, num):
                        puzzle.grid[row][col].value = num
                        if solve_puzzle(puzzle):
                            return True
                        puzzle.grid[row][col].value = 0  # Backtrack if the solution is not valid
                return False  # No valid number for this position
    return True  # Puzzle solved successfully

def check_puzzle(puzzle: Puzzle) -> bool:
    # Check if the current state of the puzzle is valid
    for row in range(9):
        for col in range(9):
            num = puzzle.grid[row][col].value
            if num != 0 and not is_valid_move(puzzle, row, col, num):
                return False
    return True

def find_all_errors(puzzle: Puzzle) -> List[Cell]:
    # Find all cells with conflicting values in the puzzle
    errors = []
    for row in range(9):
        for col in range(9):
            num = puzzle.grid[row][col].value
            if num != 0 and not is_valid_move(puzzle, row, col, num):
                errors.append(puzzle.grid[row][col])
    return errors

def find_all_empty(puzzle: Puzzle) -> List[Cell]:
    # Find all empty cells in the puzzle
    empty_cells = []
    for row in range(9):
        for col in range(9):
            if puzzle.grid[row][col].value == 0:
                empty_cells.append(puzzle.grid[row][col])
    return empty_cells

def save_puzzle_to_database(puzzle: Puzzle) -> int:
    # Convert the puzzle grid to a string for database storage
    grid_str = '\n'.join([' '.join(map(str, row)) for row in puzzle.grid])

    # Insert the puzzle into the database
    cursor.execute('INSERT INTO Puzzle (grid) VALUES (?)', (grid_str,))
    conn.commit()
    
    # Return the ID of the newly inserted puzzle
    return cursor.lastrowid

def load_puzzle_from_database(puzzle_id: int) -> Puzzle:
    # Retrieve the puzzle from the database by ID
    cursor.execute('SELECT grid FROM Puzzle WHERE id = ?', (puzzle_id,))
    result = cursor.fetchone()
    if result:
        grid_str = result[0]
        grid = [[int(cell) for cell in row.split()] for row in grid_str.split('\n')]
        return Puzzle(grid)
    else:
        return Puzzle([[0]])

@app.route('/api/sudoku/generate', methods=['POST'])
def generate_sudoku():
    # Placeholder for puzzle generation logic
    example_puzzle = Puzzle([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

    puzzle_id = save_puzzle_to_database(example_puzzle)
    return jsonify({'puzzle_id': puzzle_id})

@app.route('/api/sudoku/solve/<int:puzzle_id>', methods=['POST'])
def solve_sudoku(puzzle_id):
    puzzle = load_puzzle_from_database(puzzle_id)
    solve_puzzle(puzzle)
    return jsonify({'message': 'Puzzle solved successfully'})

@app.route('/api/sudoku/check/<int:puzzle_id>', methods=['GET'])
def check_sudoku(puzzle_id):
    puzzle = load_puzzle_from_database(puzzle_id)
    result = check_puzzle(puzzle)
    return jsonify({'valid': result})

@app.route('/api/sudoku/errors/<int:puzzle_id>', methods=['GET'])
def get_errors(puzzle_id):
    puzzle = load_puzzle_from_database(puzzle_id)
    errors = find_all_errors(puzzle)
    return jsonify({'errors': [cell.value for cell in errors]})

@app.route('/api/sudoku/empty/<int:puzzle_id>', methods=['GET'])
def get_empty_cells(puzzle_id):
    puzzle = load_puzzle_from_database(puzzle_id)
    empty_cells = find_all_empty(puzzle)
    return jsonify({'empty_cells': [cell.value for cell in empty_cells]})

if __name__ == '__main__':
    app.run(debug=True)

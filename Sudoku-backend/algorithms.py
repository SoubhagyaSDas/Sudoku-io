import sqlite3
from typing import List
from representations import Cell, Puzzle, Algorithms, History

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
    return Algorithms().IsValidMove(puzzle, row, col, num)

def solve_puzzle(puzzle: Puzzle) -> bool:
    for row in range(9):
        for col in range(9):
            if puzzle.grid[row][col].value == 0:
                for num in range(1, 10):
                    if is_valid_move(puzzle, row, col, num):
                        puzzle.grid[row][col].value = num
                        if solve_puzzle(puzzle):
                            return True
                        puzzle.grid[row][col].value = 0
                return False
    return True

def check_puzzle(puzzle: Puzzle) -> bool:
    return all(
        puzzle.grid[row][col].value == 0 or is_valid_move(puzzle, row, col, puzzle.grid[row][col].value)
        for row in range(9)
        for col in range(9)
    )

def find_all_errors(puzzle: Puzzle) -> List[Cell]:
    return [
        puzzle.grid[row][col]
        for row in range(9)
        for col in range(9)
        if puzzle.grid[row][col].value != 0 and not is_valid_move(puzzle, row, col, puzzle.grid[row][col].value)
    ]

def find_all_empty(puzzle: Puzzle) -> List[Cell]:
    return [
        puzzle.grid[row][col]
        for row in range(9)
        for col in range(9)
        if puzzle.grid[row][col].value == 0
    ]

def save_puzzle_to_database(puzzle: Puzzle) -> int:
    grid_str = '\n'.join([' '.join(map(str, row)) for row in puzzle.grid])
    cursor.execute('INSERT INTO Puzzle (grid) VALUES (?)', (grid_str,))
    conn.commit()
    return cursor.lastrowid

def load_puzzle_from_database(puzzle_id: int) -> Puzzle:
    cursor.execute('SELECT grid FROM Puzzle WHERE id = ?', (puzzle_id,))
    result = cursor.fetchone()
    return Puzzle([[int(cell) for cell in row.split()] for row in result[0].split('\n')]) if result else Puzzle([[0]])

#completed by Andrew
class Cell:
    def __init__(self):
        self.cellEntry = 0 #value of cell
        self.solution = 0
        self.row = 0
        self.col = 0
        self.notes = [] #list of notes for a single cell
        self.given = False #boolean saying if value is given by computer (initally or by hint) (will be used to determine if cell can be given by a hint)

    def GetEntry(self):
        return self.cellEntry
    
    def SetEntry(self, entry:int):
        self.cellEntry = entry

    def GetSolution(self):
        return self.solution
    
    def SetSolution(self, answer:int):
        self.solution = answer

    def GetNotes(self):
        return self.notes
    
    def SetNotes(self, notes:[]):
        self.notes = notes

    def GetRow(self):
        return self.row
    
    def GetCol(self):
        return self.col
    
    def Clear(self):
        self.cellEntry = 0

#completed by Andrew
class Puzzle:
    def __init__(self):
        self.difficulty = 0 #integer of difficulty 1=easy, 2=medium, 3=hard
        self.size = 0 #4 = 4x4, 9 = 9x9
        self.grid = Cell[self.size][self.size]

    def GetBoardSize(self):
        return self.size
    
    def SetBoardSize(self,size:int):
        self.size = size

    def GetValue(self,row,col):
        return self.grid[row][col].cellEntry
    
    def SetValue(self,row,col,value):
        self.grid[row][col].cellEntry = value

    def GetNotes(self,row,col):
        return self.grid[row][col].notes
    
    def SetNotes(self,row,col,notes):
        self.grid[row][col].notes = notes

    def GetDifficulty(self):
        return self.difficulty
    
    def SetDifficulty(self,difficulty):
        self.difficulty = difficulty

    def ResetCell(self,row,col): #called when user wants to remove value from a cell (enters same value as is in cell)
        self.grid[row][col].Clear()

    #IsLegal() ????? or IsValid(row,col):bool from prof class diagram

#completed by Andrew
class HxEntry:
    def __init__(self):
        self.oldCell = Cell
        self.newCell = Cell
        self.isCorrect = True #checks if puzzle is correct as of most recent move/entry
        self.puzzle = Puzzle

    def CreateEntry(self,old,new,status):
        self.oldCell = old
        self.newCell = new
        self.isCorrect = status

    def SetCorrectness(self,puzzle): #using algo check correctness of puzzle
        self.isCorrect = CheckPuzzle(puzzle)
    #GetCell() and IsCorrect() ??? I don't get what these are supposed to do

#completed by Andrew
class History:
    def __init__(self):
        self.history = [] #will be a list of HxEntry elements

    def AddToHistory(self, entry:HxEntry):
        self.history.append(entry)

    def PopLastMove(self):
        return self.history.pop()
    
#completed by Nashrah
class Algorithms:
    def IsValidMove(self,puzzle: Puzzle, row: int, col: int, num: int) -> bool:
        # Check if placing the number at the given position is a valid move
        for i in range(9):
            if puzzle.grid[row][i].cellEntry == num or puzzle.grid[i][col].cellEntry == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if puzzle.grid[start_row + i][start_col + j].cellEntry == num:
                    return False

        return True
    
    def SolvePuzzle(self,puzzle: Puzzle) -> bool:
        # Recursive backtracking algorithm to solve the Sudoku puzzle
        for row in range(9):
            for col in range(9):
                if puzzle.grid[row][col].cellEntry == 0:
                    for num in range(1, 10):
                        if self.IsValidMove(puzzle, row, col, num):
                            puzzle.grid[row][col].cellEntry = num
                            if self.SolvePuzzle(puzzle):
                                return True
                            puzzle.grid[row][col].cellEntry = 0  # Backtrack if the solution is not valid
                    puzzle.grid[row][col].SetSolution(num) #once backtracking is done and the solution to the cell is found, store the solution of the cell
                    return False  # No valid number for this position
        return True  # Puzzle solved successfully

    def CheckPuzzle(self,puzzle: Puzzle) -> bool:
        # Check if the current state of the puzzle is valid
        for row in range(9):
            for col in range(9):
                num = puzzle.grid[row][col].cellEntry
                if num != 0 and not self.IsValidMove(puzzle, row, col, num):
                    return False
        return True

    def FindAllErrors(self,puzzle: Puzzle) -> List[Cell]:
        # Find all cells with conflicting values in the puzzle
        errors = []
        for row in range(9):
            for col in range(9):
                num = puzzle.grid[row][col].cellEntry
                if num != 0 and not self.IsValidMove(puzzle, row, col, num):
                    errors.append(puzzle.grid[row][col])
        return errors

    def FindAllEmpty(puzzle: Puzzle) -> List[Cell]:
        # Find all empty cells in the puzzle
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if puzzle.grid[row][col].cellEntry == 0:
                    empty_cells.append(puzzle.grid[row][col])
        return empty_cells
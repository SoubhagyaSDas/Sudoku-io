#completed by Andrew
import math
class Cell:
    def __init__(self):
        self.cellEntry = 0 #value of cell
        self.solution = 0
        self.row = 0
        self.col = 0
        self.notes = [] #list of notes for a single cell
        self.given = False #boolean saying if value is given by computer (initally or by hint) (will be used to determine if cell can be given by a hint) (given=True is a sign of correctness)

    def GetEntry(self):
        return self.cellEntry
    
    def SetEntry(self, entry:int):
        #if self.given == False:
        self.cellEntry = entry

    def GetSolution(self):
        return self.solution
    
    def SetSolution(self, answer:int):
        self.solution = answer

    def GetNotes(self):
        return self.notes
    
    def SetNotes(self, note):
        if note in self.notes:
            self.notes.remove(note)
        else:
            self.notes.append(note)
            self.notes.sort()

    def GetRow(self):
        return self.row
    
    def GetCol(self):
        return self.col
    
    def Clear(self):
        self.cellEntry = 0

    def SetGiven(self):
        self.given = True

#completed by Andrew
class Puzzle:
    def __init__(self):
        self.difficulty = "Easy"  #easy, medium, or hard
        self.size = 9 #4 = 4x4, 9 = 9x9
        #self.grid = Cell[self.size][self.size]
        self.boardID = 0
        self.grid = [[]]

    def GetBoardSize(self):
        return self.size
    
    def SetBoardSize(self,size:int):
        self.size = size

    def GetBoardID(self):
        return self.boardID
    
    def SetBoardID(self,boardID:int):
        self.boardID = boardID

    def GetValue(self,row,col):
        return self.grid[row][col].GetEntry()

    def SetCell(self,row,col,value):
        #HxEntry.oldCell = self.grid[row][col]
        if self.grid[row][col].GetEntry() == value: #if the user enters the same value into the same cell again it means they want to clear the cell (make it blank)
            self.ResetCell(row,col)
            return True
        elif self.grid[row][col].given == False:
            self.grid[row][col].SetEntry(value)
            return True
        else:
            return False
        #HxEntry.newCell = self.grid[row][col]
        #HxEntry.SetCorrectness(self)

    def GetCell(self,row,col):
        return self.grid[row][col]
    
    '''def SetCell(self,row,col,value,cell):
        #self.grid[row][col] = cell
        cell.row = row
        cell.col = col
        cell.GetEntry() = value'''

    def GetNotes(self,row,col):
        return self.grid[row][col].GetNotes()
    
    def SetNotes(self,row,col,note):
        self.grid[row][col].SetNotes(note)

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

    def IsCorrect(self,puzzle,algo): #using algo check correctness of puzzle
        return algo.CheckCorrectnessOfPuzzleForHistory(puzzle)
    #GetCell() ??? I don't get what this is supposed to do

#completed by Andrew
class History:
    def __init__(self):
        self.history = [] #will be a list of HxEntry elements

    def AddToHistory(self, entry:HxEntry):
        self.history.append(entry)

    def PopLastMove(self):
        return self.history.pop()
    
    def ClearFromHistory(self, cell:Cell): #used when a hint is given or when check puzzle is called and correct moves are made hardwired (given) meaning any past move involving that cell should be removed from history (no need for those moves to be undone)
        self.history = list(filter(lambda histItem: histItem.newCell.row != cell.row or histItem.newCell.col != cell.col,self.history))

    def RecreateHistory(self,puzzle:Puzzle,algo):
        #print statements commented out below were to check outputs at various stages
        reverseHistory = []
        #print(self.history)
        for move in self.history:
            #print(move)
            reverseHistory.append(self.PopLastMove())
        
        #print(reverseHistory)

        fixedHistory = []
        for entry_to_recheck in reverseHistory:
            #print(entry_to_recheck.oldCell,entry_to_recheck.newCell)
            entry_to_recheck.CreateEntry(entry_to_recheck.oldCell,entry_to_recheck.newCell,entry_to_recheck.IsCorrect(puzzle,algo))
            #print(entry_to_recheck)
            fixedHistory.append(entry_to_recheck)

        self.history = fixedHistory

#completed by Nashrah, edited by Andrew
class Algorithms:
    def CheckCorrectnessOfPuzzle(self,puzzle:Puzzle,history:History):
        wrongCells = []
        rightCells = []
        for row in range(puzzle.GetBoardSize()):
            for col in range(puzzle.GetBoardSize()):
                #the move is wrong
                if puzzle.grid[row][col].GetEntry() != 0 and puzzle.grid[row][col].GetEntry() != puzzle.grid[row][col].solution and not puzzle.grid[row][col].given:
                    #wrongCells.append(puzzle.grid[row][col])
                    wrongCells.append({"row":row,"col":col})
                #the move is right
                elif puzzle.grid[row][col].GetEntry() != 0 and puzzle.grid[row][col].GetEntry() == puzzle.grid[row][col].solution and not puzzle.grid[row][col].given:
                    puzzle.grid[row][col].SetGiven()
                    history.ClearFromHistory(puzzle.grid[row][col]) #clear move from history such that it isn't looked at when trying to give a hint
                    #rightCells.append(puzzle.grid[row][col])
                    rightCells.append({"row":row,"col":col})
        return wrongCells,rightCells
    
    def CheckCorrectnessOfPuzzleForHistory(self,puzzle:Puzzle):
        gameWon = True
        for row in range(puzzle.GetBoardSize()):
            for col in range(puzzle.GetBoardSize()):
                if puzzle.grid[row][col].GetEntry() == 0:
                    gameWon = False
                if puzzle.grid[row][col].GetEntry() != 0 and puzzle.grid[row][col].GetEntry() != puzzle.grid[row][col].solution and not puzzle.grid[row][col].given:
                    return False
        if gameWon == True:
            return "Game Won!"
        return True

    def IsValidMove(self,puzzle: Puzzle, row: int, col: int, num: int) -> bool:
        # Check if placing the number at the given position is a valid move
        for i in range(puzzle.GetBoardSize()):
            if puzzle.grid[row][i].GetEntry() == num or puzzle.grid[i][col].GetEntry() == num:
                return False

        start_row, start_col = int(math.sqrt(puzzle.GetBoardSize())) * (row // int(math.sqrt(puzzle.GetBoardSize()))), int(math.sqrt(puzzle.GetBoardSize())) * (col // int(math.sqrt(puzzle.GetBoardSize())))
        for i in range(int(math.sqrt(puzzle.GetBoardSize()))):
            for j in range(int(math.sqrt(puzzle.GetBoardSize()))):
                if puzzle.grid[start_row + i][start_col + j].GetEntry() == num:
                    return False

        return True
    
    def SolvePuzzle(self,puzzle: Puzzle) -> bool:
        # Recursive backtracking algorithm to solve the Sudoku puzzle
        for row in range(puzzle.GetBoardSize()):
            for col in range(puzzle.GetBoardSize()):
                if puzzle.grid[row][col].GetEntry() == 0:
                    for num in range(1, puzzle.GetBoardSize()+1):
                        if self.IsValidMove(puzzle, row, col, num):
                            puzzle.grid[row][col].SetEntry(num)
                            if self.SolvePuzzle(puzzle):
                                return True
                            puzzle.grid[row][col].SetEntry(0)  # Backtrack if the solution is not valid
                    puzzle.grid[row][col].SetSolution(num) #once backtracking is done and the solution to the cell is found, store the solution of the cell
                    return False  # No valid number for this position
                else:
                    puzzle.grid[row][col].SetSolution(puzzle.grid[row][col].GetEntry())
        return True  # Puzzle solved successfully

    '''def CheckPuzzle(self,puzzle: Puzzle) -> bool:
        # Check if the current state of the puzzle is valid
        for row in range(9):
            for col in range(9):
                num = puzzle.grid[row][col].GetEntry()
                if num != 0 and not self.IsValidMove(puzzle, row, col, num):
                    return False
        return True'''

    def FindAllErrors(self,puzzle: Puzzle) -> list[Cell]:
        # Find all cells with conflicting values in the puzzle
        errors = []
        for row in range(puzzle.GetBoardSize()):
            for col in range(puzzle.GetBoardSize()):
                num = puzzle.grid[row][col].GetEntry()
                if num != 0 and num != puzzle.grid[row][col].solution:
                    errors.append(puzzle.grid[row][col])
        return errors

    def FindAllEmpty(self,puzzle: Puzzle) -> list[Cell]:
        # Find all empty cells in the puzzle
        empty_cells = []
        for row in range(puzzle.GetBoardSize()):
            for col in range(puzzle.GetBoardSize()):
                if puzzle.grid[row][col].GetEntry() == 0:
                    empty_cells.append(puzzle.grid[row][col])
        return empty_cells
    
import random

#completed by Andrew
class GameEngine:
    def __init__(self):
        self.puzzle = Puzzle()
        self.currentValue = 0
        self.history = History()
        self.algo = Algorithms()

    def Undo(self):
        if self.history: #moves exist in history stack
            return self.history.PopLastMove()
        else: #history stack is empty
            return

    def UndoUntilCorrect(self):
        numToPop = 0
        movesToUndo = []
        for move in reversed(self.history.history):
            #print(move)  print statements were to see how HxEntrys were being itereated through
            #print(move.isCorrect)   since self.history.history is a list and not a stack here, had to use reversed() for LIFO
            if move.isCorrect == False:
                #print("IM IN IF PART")
                numToPop+=1
            else:
                break
        for i in range(numToPop):
            movesToUndo.append(self.Undo())

        return movesToUndo

    def GetCurrentValue(self):
        return self.currentValue

    def SetCurrentValue(self,val):
        self.currentValue = val

    def GetRandomHint(self): #what should be returned from hint functions a Cell or just row,col,solution???
        errors = self.algo.FindAllErrors(self.puzzle)
        empty = self.algo.FindAllEmpty(self.puzzle)
        if errors: #see if there are errors to fix with a hint first
            randErrorIndex = random.randint(0,len(errors)-1)
            errorToFix = errors[randErrorIndex] #then return the a random cell with an error
            self.puzzle.grid[errorToFix.row][errorToFix.col].SetEntry(errorToFix.solution)
            self.puzzle.grid[errorToFix.row][errorToFix.col].SetGiven()
            self.history.ClearFromHistory(errorToFix)
            self.history.RecreateHistory(self.puzzle,self.algo)
            return errorToFix.row, errorToFix.col, errorToFix.solution
        elif not errors and empty: #no user-entered errors but empty cells exist
            randEmptyIndex = random.randint(0,len(empty))
            emptyToFill = empty[randEmptyIndex]
            self.puzzle.grid[emptyToFill.row][emptyToFill.col].SetEntry(emptyToFill.solution)
            self.puzzle.grid[emptyToFill.row][emptyToFill.col].SetGiven()
            return emptyToFill.row, emptyToFill.col, emptyToFill.solution
        else: #all user-entered values are right and no empty cells exist (puzzle should end successfully)
            return
        
    def GetSpecificHint(self,row,col):
        if self.puzzle.grid[row][col].given == False:
            self.puzzle.grid[row][col].SetEntry(self.puzzle.grid[row][col].solution)
            self.puzzle.grid[row][col].SetGiven()
            self.history.ClearFromHistory(self.puzzle.grid[row][col])
            self.history.RecreateHistory(self.puzzle,self.algo)
            return row,col,self.puzzle.grid[row][col].solution
        else: #user clicked on given/hardwired cell for specific hint, nothing should happen/be returned
            return 
    
    def CallCheckCorrectnessOfPuzzle(self): #is this function needed???
        self.algo.CheckCorrectnessOfPuzzle(self.puzzle)
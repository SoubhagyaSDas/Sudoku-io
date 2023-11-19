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

class HxEntry:
    def __init__(self):
        self.oldCell = Cell
        self.newCell = Cell
        self.isCorrect = True #checks if puzzle is correct as of most recent move/entry

    def CreateEntry(self,old,new,status):
        self.oldCell = old
        self.newCell = new
        self.isCorrect = status

    #GetCell() and IsCorrect() ??? I don't get what these are supposed to do

class History:
    def __init__(self):
        self.history = [] #will be a list of HxEntry elements

    def AddToHistory(self, entry):
        self.history.append(entry)

    def PopLastMove(self):
        return self.history.pop()
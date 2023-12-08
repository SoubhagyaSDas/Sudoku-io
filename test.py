#full test.py completed by Andrew
#see commented out lines and print statements for documentation

import representations as r

#testing setting up a puzzle and its cells
#this test has the puzzle.grid as a 2d array/list of integers
'''example_puzzle = r.Puzzle()
example_puzzle.grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
example_puzzle.SetBoardSize(9)
example_puzzle.SetDifficulty(1)

print(example_puzzle.GetDifficulty())
print(example_puzzle.GetBoardSize())
print(example_puzzle.grid)

entries = []
for row in range(9):
    for col in range(9):
        entries.append(example_puzzle.grid[row][col])

cellsList = [r.Cell() for i in range(example_puzzle.size*example_puzzle.size)]
#print(cellsList)

i=0
for row in range(example_puzzle.size):
    for col in range(example_puzzle.size):
        example_puzzle.SetCell(row,col,entries[i],cellsList[i])
        i+=1

print(cellsList[3].GetEntry())
print(cellsList[2].solution)

algo = r.Algorithms()

#algo.SolvePuzzle(example_puzzle) #problem encountered here with access to puzzle.grid[row][col].GetEntry()

print(cellsList[2].solution)'''

###PUZZLE CLASS FUNCTION TESTING###
#this test has puzzle.grid as a 2d array/list of Cell objects
#i believe this is the correct implementation
import numpy as np
sample_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

entries = []
for row in range(9):
    for col in range(9):
        entries.append(sample_puzzle[row][col])

#create a list of Cells to fit entire board
cellsList = [r.Cell() for i in range(81)]

#fill in entry values of created Cells list and set row and col values and set given/hardwired = True for given values (entry!=0)
i=0
for row in range(9):
    for col in range(9):
        cellsList[i].SetEntry(entries[i])
        if entries[i]!=0:
            cellsList[i].SetGiven()
        cellsList[i].row = row
        cellsList[i].col = col
        i+=1

def ResetCells(lst):
    i=0
    for row in range(9):
        for col in range(9):
            lst[i].SetEntry(entries[i])
            lst[i].row = row
            lst[i].col = col
            i+=1

puzzleObj = r.Puzzle()

#convert 1d array of Cells into 2d to be stored as puzzle.grid
puzzleObj.grid = np.array(cellsList).reshape(9,9)

#check if 2d puzzle matrix is set up correctly (check that each cellEntry has a value based on provided puzzle)
for row in range(9):
    for col in range(9):
        print(puzzleObj.GetValue(row,col),puzzleObj.grid[row][col].GetRow(),puzzleObj.grid[row][col].GetCol())

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j].GetEntry())
            else:
                print(str(board[i][j].GetEntry()) + " ", end="")

def print_sol_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j].solution)
            else:
                print(str(board[i][j].solution) + " ", end="")

#testing of setting and getting puzzle properties (size and difficulty)
puzzleObj.SetBoardSize(9)
puzzleObj.SetDifficulty("Hard")
print()
print("Puzzle is a ",puzzleObj.GetBoardSize(),"x",puzzleObj.GetBoardSize(), " grid")
print()
print("Puzzle is ",puzzleObj.GetDifficulty()," difficulty")
print()

#test puzzle.grid to see if values stored correctly
print("ORIGINAL BOARD")
print_board(puzzleObj.grid)
#test solver algorithm and storing of Cell.solution values
algo = r.Algorithms()
algo.SolvePuzzle(puzzleObj)
print()
print("SOLVED BOARD")
print_sol_board(puzzleObj.grid)

#test set and get cell functions and set and get notes functions (regardless of order notes are put in, return them in numerical order)
puzzleObj.SetNotes(0,2,1) #set a note of '1' in cell[0][2]
print()
print("After setting a note of '1', the notes for cell in row ",puzzleObj.grid[0][2].GetRow()," column ",puzzleObj.grid[0][2].GetCol(), " are ",puzzleObj.GetNotes(0,2))
puzzleObj.SetNotes(0,2,4) #set a note of '4' in cell[0][2]
print()
print("After setting a note of '4', the notes for cell in row ",puzzleObj.grid[0][2].GetRow()," column ",puzzleObj.grid[0][2].GetCol(), " are ",puzzleObj.GetNotes(0,2))
puzzleObj.SetNotes(0,2,2) #set a note of '2' in cell[0][2]
print()
print("After setting a note of '2', the notes for cell in row ",puzzleObj.grid[0][2].GetRow()," column ",puzzleObj.grid[0][2].GetCol(), " are ",puzzleObj.GetNotes(0,2))
print()
print("The notes for cell in row ",puzzleObj.grid[0][2].GetRow()," column ",puzzleObj.grid[0][2].GetCol(), " are ",puzzleObj.GetNotes(0,2))
print()
puzzleObj.SetNotes(0,2,1) #removing the note '1' from cell[0][2]
print("After removing the note '1' (by clicking on '1' again in note mode), the notes for cell in row ",puzzleObj.grid[0][2].GetRow()," column ",puzzleObj.grid[0][2].GetCol(), " are ",puzzleObj.GetNotes(0,2))
print()
#Testing user input and 'given' attribute values 
print("BOARD WITH USER INPUT '2' IN ROW 0 COLUMN 2")
ResetCells(cellsList) #need to reset cellEntries from being set to solution
puzzleObj.SetCell(0,2,2)
print_board(puzzleObj.grid)
print()
print("CHECKING GIVEN VARIABLE OF CELLS")
print("For 0 row 0 col cell (should be True)", puzzleObj.grid[0][0].given)
print("For 0 row 3 col cell (should be False)", puzzleObj.grid[0][3].given)
print("For 0 row 2 col cell (should be False)", puzzleObj.grid[0][2].given)
ResetCells(cellsList) #manually undo the "2" move before testing undo functionality below
print("BOARD WITH FORCED UNDOING OF LAST MOVE. BOARD IS RESET")
print_board(puzzleObj.grid)

#test history and hxentry functionality
histEnt = r.HxEntry()
hist = r.History()
engine = r.GameEngine()
engine.puzzle=puzzleObj
engine.history=hist
engine.algo=algo
#backend will receive row,col,user-entered value for a cell
#history has to record current cell value (before user input), new cell value (with user input) and if the puzzle is correct
#assume JSON object of {row:0,col:2,value:4} was received
import copy
userMoveRow = 0
userMoveCol = 2
userMoveVal = 4
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else: 
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '4' IN ROW 0 COL 2")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
    print()
    print("ADDRESSES OF HxEntry OBJECTS IN HISTORY")
    print(engine.history.history)
#each time a move is made anytime something is added to history stack; a new HxEntry object has to be created
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 3
userMoveVal = 8
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '8' IN ROW 0 COL 3")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
    print()
    print("ADDRESSES OF HxEntry OBJECTS IN HISTORY")
    print(engine.history.history)

histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 6
userMoveVal = 9
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '9' IN ROW 0 COL 6")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
    print()
    print("ADDRESSES OF HxEntry OBJECTS IN HISTORY")
    print(engine.history.history)

histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 3
userMoveVal = 6
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '6' IN ROW 0 COL 3")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
    print()
    print("ADDRESSES OF HxEntry OBJECTS IN HISTORY")
    print(engine.history.history)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#test game engine functionality
#i think for each move, the user entered value has to be set to GameEngine.currentValue
#UNDO
#print(engine.Undo()) #checking that popped HxEntry gets returned
undoneMove = engine.Undo()
print("Undone move address: ",undoneMove)
engine.puzzle.SetCell(undoneMove.oldCell.row,undoneMove.oldCell.col,undoneMove.oldCell.GetEntry())
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("SEE PUZZLE BOARD WITH MOST RECENT MOVE UNDONE")
print_board(engine.puzzle.grid)
print()

#UNDO UNTIL CORRECT
undoneMoves = engine.UndoUntilCorrect()
print("Undone moves addresses: ",undoneMoves)
for move in undoneMoves:
    print("UNDOING THIS MOVE AS PART OF UndoUntilCorrect() (formatted row,col,value)")
    print(move.oldCell.row,move.oldCell.col,move.newCell.GetEntry())
    engine.puzzle.SetCell(move.oldCell.row,move.oldCell.col,move.oldCell.GetEntry())
print()
print("PUZZLE BOARD WITH MOST RECENT STATUS OF WHEN FULL PUZZLE WAS CORRECT")
print_board(engine.puzzle.grid)

#CHECK CORRECT OF PUZZLE (CHECK SOLUTION BUTTON)
#I will put in some moves (right and wrong) and check solution 

#right move, puzzle is correct so far
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 3
userMoveVal = 6
engine.SetCurrentValue(userMoveVal)    
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '6' IN ROW 0 COL 3")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#wrong move, puzzle is wrong
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 5
userMoveVal = 3
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '3' IN ROW 0 COL 5")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#wrong move, puzzle is wrong (but this move will be righted in next move) (did this to see if ClearFromHistory() will remove both times this cell was affected in history)
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 6
userMoveVal = 7
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '7' IN ROW 0 COL 6")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#right move, puzzle is wrong
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 6
userMoveVal = 9
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '9' IN ROW 0 COL 6")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#wrong move, puzzle is wrong
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 7
userMoveVal = 2
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '2' IN ROW 0 COL 7")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#this move is as if the user manually undid a move by entering in the same value into a cell they already filled in with that value
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 3
userMoveVal = 6
engine.SetCurrentValue(userMoveVal)
#print(engine.GetCurrentValue(),engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry(),engine.puzzle.grid[userMoveRow][userMoveCol].given)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '6' IN ROW 0 COL 3")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("AFTER CELL AT ROW 0 COLUMN 3 WAS RESET BY PUTTING IN SAME NUMBER")
print()
print_board(puzzleObj.grid)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#TEST CHECK CORRECTNESS OF PUZZLE FUNCTIONALITY (if user pressed "check solution" button)
wrongMoves=[]
rightMoves=[]
#checking given values of right moves before checking correctness (should be false)
#below test was ran BEFORE History.ClearFromHistory() was added to Algoithms.CheckCorrectnessOfPuzzle() function
#output was correct showing all 6 moves shown in history having given value of false
#then after running CheckCorrectnessOfPuzzle(), the correct moves had their given values changed to "True"
#***if you want to run this test again, comment out where ClearFromHistory() is called in CheckCorrectnessOfPuzzle() in representations.py***
print()
print("THIS SECTION WILL HAVE DIFFERENT RESULTS IF ClearFromHistory() function call is commented out of CheckCorrectnessOfPuzzle() function")
print("'given' variable for these 5 moves should all be false (formatted row, col, user entry, solution, is given/hardwired?)")
print(engine.history.history) #did this to see that in ClearFromHistory() i made history a 'filter' object than is not iterable. I had to wrap it in list()
for ele in engine.history.history:
    print(ele.newCell.row,ele.newCell.col,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].GetEntry(),engine.puzzle.grid[ele.newCell.row][ele.newCell.col].solution,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].given)
wrongMoves,rightMoves = engine.algo.CheckCorrectnessOfPuzzle(engine.puzzle,engine.history)
print("From 5 moves made so far, the first and fourth moves are correct. The second, third, and fifth moves are wrong")
print()
print("The cells of the incorrect moves are ",wrongMoves)
print("The cells of the correct moves are ",rightMoves)
print()
print("After clicking 'check solution/check puzzle' the given variables for the correct moves should now be true")
print("'given' variable for 2 correct cells (0,2), (0,6) should all be true and for 2 incorrect cells (0,5), (0,7) should be false (formatted row, col, user entry, solution, is given/hardwired?)")
for ele in engine.history.history:
    print(ele.newCell.row,ele.newCell.col,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].GetEntry(),engine.puzzle.grid[ele.newCell.row][ele.newCell.col].solution,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].given)

print("The cells printed in the above two lists may look different from moves in history since I am returning the current state of the cell instead of each unique move.")

#RANDOM HINT
#at this point in test, after just checking the puzzle, there are only 2 wrong moves that remain (as shown in history stack)
#random hint will look at fixing user errors (at random) first before returning a hint for a ranomd empty cell
#this random hint will return one of the user-inputted wrong cells
print()
print("AFTER CALLING RANDOM HINT, THIS USER-ENTERED WRONG CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
#print(randHint[0]) #the row of hint cell ([1] would be column, [2] would be solution)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#this random hint will return the other user-inputted wrong cell
print()
print("AFTER CALLING RANDOM HINT, THIS USER-ENTERED WRONG CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#this random hint will return a random empty cell's location and soltion since no more user errors remain
print()
print("AFTER CALLING RANDOM HINT, THIS EMPTY CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("CURRENT BOARD STATUS AFTER RANDOM HINTS (FIXING TWO USER ERRORS AND GIVING ONE EMPTY CELL)")
print_board(puzzleObj.grid)
print()

#SPECIFIC HINT
#trying to get a specific hint for an original given cell
specHint = engine.GetSpecificHint(0,0)
print("CALLING SPECIFIC HINT OF ORIGINAL GIVEN CELL")
print(specHint) #should be None
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print()
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#trying to get a specific hint for a user entered answer that was checked and is correct
specHint = engine.GetSpecificHint(0,2)
print("CALLING SPECIFIC HINT OF USER-ENTERED CELL THAT WAS CHECKED AS CORRECT")
print(specHint) #should be None
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print()
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#trying to get a specific hint for a solution provided by a random hint
specHint = engine.GetSpecificHint(0,7)
print("CALLING SPECIFIC HINT OF CELL SOLVED BY RANDOM HINT")
print(specHint) #should be None
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print()
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#make a right move
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 8
userMoveVal = 2
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '2' IN ROW 0 COL 8")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect) 

#make a wrong move
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 3
userMoveVal = 1
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
    newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
    print()
    print("BOARD WITH USER MOVE OF '1' IN ROW 0 COL 3")
    print_board(engine.puzzle.grid)
    print()
    print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
    print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
    engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#trying to get a specific hint for the right move (which user doesn't know is right)
specHint = engine.GetSpecificHint(0,8)
print()
print("CALLING SPECIFIC HINT OF USER-ENTERED UNCHECKED CORRECT MOVE")
print(specHint) #should be (0,8,2) (which is what the user entered but now they know it is right)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#trying to get a specific hint for the wrong move (which user doesn't know is wrong)
specHint = engine.GetSpecificHint(0,3)
print()
print("CALLING SPECIFIC HINT OF USER-ENTERED UNCHECKED INCORRECT MOVE")
print(specHint) #should be (0,3,6) (user entered a '1' in this spot instead of the correct '6')
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#trying to get a specific hint for the wan empty cell
specHint = engine.GetSpecificHint(8,0)
print()
print("CALLING SPECIFIC HINT OF USER-SELECTED EMPTY CELL")
print(specHint) #should be (0,3,6) (user entered a '1' in this spot instead of the correct '6')
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("BOARD WITH USER-ENTERED RIGHT MOVE, USER-ENTERED WRONG MOVE, AND AN EMPTY CELL SOLVED WITH SPECIFIC HINT")
print_board(puzzleObj.grid)

#try to edit a hardwired/given cell
print()
print("USER TRYING TO EDIT A HARDWIRED/GIVEN CELL (nothing should be added to history (history should be empty at this point))")
histEnt=r.HxEntry()
userMoveRow = 0
userMoveCol = 0
userMoveVal = 9
engine.SetCurrentValue(userMoveVal)
if engine.GetCurrentValue() == engine.puzzle.grid[userMoveRow][userMoveCol].GetEntry() and engine.puzzle.grid[userMoveRow][userMoveCol].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
    engine.puzzle.ResetCell(userMoveRow,userMoveCol)
    engine.history.ClearFromHistory(engine.puzzle.grid[userMoveRow][userMoveCol])
else:
    oldCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
    if engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal):
        engine.puzzle.SetCell(userMoveRow,userMoveCol,userMoveVal)
        newCell = copy.deepcopy(engine.puzzle.grid[userMoveRow][userMoveCol])
        histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
        print()
        print("BOARD WITH USER MOVE OF '9' IN ROW 0 COL 0")
        print_board(engine.puzzle.grid)
        print()
        print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
        print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
        engine.history.AddToHistory(histEnt)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)
print()

def MakeAMove(row,col,val):
    histEnt=r.HxEntry()
    engine.SetCurrentValue(val)
    if engine.GetCurrentValue() == engine.puzzle.grid[row][col].GetEntry() and engine.puzzle.grid[row][col].given == False: #if user wants to make a cell blank again by entering the value that is already there (that they put there)
        engine.puzzle.ResetCell(row,col)
        engine.history.ClearFromHistory(engine.puzzle.grid[row][col])
    else:
        oldCell = copy.deepcopy(engine.puzzle.grid[row][col])
        print("user inputted row and col of cell they want to edit and value they want to enter: ",row,col,val)
        print("current cell status (row,col,current value, given?): ",engine.puzzle.grid[row][col].GetRow(),engine.puzzle.grid[row][col].GetCol(),engine.puzzle.grid[row][col].GetEntry(),engine.puzzle.grid[row][col].given)
        print("what is returned from puzzle.SetCell(): ", engine.puzzle.SetCell(row,col,val))
        if engine.puzzle.SetCell(row,col,val):
            engine.puzzle.SetCell(row,col,val)
            newCell = copy.deepcopy(engine.puzzle.grid[row][col])
            histEnt.CreateEntry(oldCell,newCell,histEnt.IsCorrect(engine.puzzle,engine.algo))
            print()
            print("BOARD WITH USER MOVE OF",val,"IN ROW",row,"COL",col)
            print_board(engine.puzzle.grid)
            print()
            print("HISTORY ELEMENT REFLECTING PAST MOVE (old row, old col, old value, new row, new col, new value, is puzzle correct?)")
            print(histEnt.oldCell.row,histEnt.oldCell.col,histEnt.oldCell.GetEntry(),histEnt.newCell.row,histEnt.newCell.col,histEnt.newCell.GetEntry(),histEnt.isCorrect)
            engine.history.AddToHistory(histEnt)
    print()
    print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
    for ele in engine.history.history:
        print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)
    print()

#testing making moves with above function

print("TESTING MAKING MOVES WITH A FUNCTION")
MakeAMove(0,3,9)
MakeAMove(1,8,3)
MakeAMove(2,0,1)

#test recreate history functionality (after a hint is given, recheck remaining moves in history stack)
#right now two moves in history stack in this order
#first move wrong, second move right --> so puzzle is wrong after 1st move, and puzzle is still wrong after second move
#after calling random hint, which should correct 1st wrong move, should remove it from history, recheck the one remaining move (the 2nd correct move), see that the puzzle is correct, and say True in hsitory stack

print()
print("AFTER CALLING RANDOM HINT, THE CELL AT ROW 1 COLUMN 8 AND ITS SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
print()
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print("HERE THE REMAINING MOVE HAS BEEN RECHECKED AND SHOULD SAY TRUE SINCE IT IS A CORRECT MOVE AND THE ONLY MOVE")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("CURRENT BOARD STATUS AFTER RANDOM HINT")
print_board(puzzleObj.grid)
print()
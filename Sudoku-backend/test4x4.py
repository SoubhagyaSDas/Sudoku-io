import representations as r

import numpy as np
sample_puzzle = [
        [0, 1, 0, 0],
        [3, 0, 0, 1],
        [4, 0, 0, 2],
        [0, 0, 4, 0]
    ]

entries = []
for row in range(4):
    for col in range(4):
        entries.append(sample_puzzle[row][col])

#create a list of Cells to fit entire board
cellsList = [r.Cell() for i in range(16)]

#fill in entry values of created Cells list and set row and col values and set given/hardwired = True for given values (entry!=0)
i=0
for row in range(4):
    for col in range(4):
        cellsList[i].SetEntry(entries[i])
        if entries[i]!=0:
            cellsList[i].SetGiven()
        cellsList[i].row = row
        cellsList[i].col = col
        i+=1

def ResetCells(lst):
    i=0
    for row in range(4):
        for col in range(4):
            lst[i].SetEntry(entries[i])
            lst[i].row = row
            lst[i].col = col
            i+=1

puzzleObj = r.Puzzle()

#convert 1d array of Cells into 2d to be stored as puzzle.grid
puzzleObj.grid = np.array(cellsList).reshape(4,4)

#check if 2d puzzle matrix is set up correctly (check that each cellEntry has a value based on provided puzzle)
for row in range(4):
    for col in range(4):
        print(puzzleObj.GetValue(row,col),puzzleObj.grid[row][col].GetRow(),puzzleObj.grid[row][col].GetCol())

def print_board(board):
    for i in range(len(board)):
        if i % 2 == 0 and i != 0:
            print("- - - - - - ")

        for j in range(len(board[0])):
            if j % 2 == 0 and j != 0:
                print(" | ", end="")

            if j == 3:
                print(board[i][j].GetEntry())
            else:
                print(str(board[i][j].GetEntry()) + " ", end="")

def print_sol_board(board):
    for i in range(len(board)):
        if i % 2 == 0 and i != 0:
            print("- - - - - - ")

        for j in range(len(board[0])):
            if j % 2 == 0 and j != 0:
                print(" | ", end="")

            if j == 3:
                print(board[i][j].solution)
            else:
                print(str(board[i][j].solution) + " ", end="")

#testing of setting and getting puzzle properties (size and difficulty)
puzzleObj.SetBoardSize(4)
puzzleObj.SetDifficulty("Easy")
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
print("For 0 row 1 col cell (should be True)", puzzleObj.grid[0][1].given)
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

#MAKE MOVES
MakeAMove(2,1,1)
MakeAMove(1,1,4)
MakeAMove(0,3,3)
MakeAMove(0,3,2)
MakeAMove(0,1,4) #can't be done since that cell is given

#UNDO A MOVE
undoneMove = engine.Undo()
print("Undone move: ",undoneMove.oldCell.row,undoneMove.oldCell.col,undoneMove.oldCell.GetEntry(),undoneMove.newCell.row,undoneMove.newCell.col,undoneMove.newCell.GetEntry(),undoneMove.isCorrect)
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
#print("Undone moves addresses: ",undoneMoves)
for move in undoneMoves:
    print("UNDOING THIS MOVE AS PART OF UndoUntilCorrect() (formatted row,col,value)")
    print(move.oldCell.row,move.oldCell.col,move.newCell.GetEntry())
    engine.puzzle.SetCell(move.oldCell.row,move.oldCell.col,move.oldCell.GetEntry())
print()
print("PUZZLE BOARD WITH MOST RECENT STATUS OF WHEN FULL PUZZLE WAS CORRECT")
print_board(engine.puzzle.grid)

#CHECK PUZZLE CORRECTNESS

MakeAMove(2,1,1)
MakeAMove(1,1,4) #this is the only correct move
MakeAMove(0,3,3)
MakeAMove(0,3,2)
MakeAMove(0,1,4) #can't be done since that cell is given

wrongMoves=[]
rightMoves=[]

print()
#print(engine.history.history) #did this to see that in ClearFromHistory() i made history a 'filter' object than is not iterable. I had to wrap it in list()
for ele in engine.history.history:
    print(ele.newCell.row,ele.newCell.col,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].GetEntry(),engine.puzzle.grid[ele.newCell.row][ele.newCell.col].solution,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].given)
wrongMoves,rightMoves = engine.algo.CheckCorrectnessOfPuzzle(engine.puzzle,engine.history)
print("From 4 moves made so far, the second move is correct. The rest are wrong")
print()
print("The cells of the incorrect moves are ",wrongMoves)
print("The cells of the correct moves are ",rightMoves)
print()
print("After clicking 'check solution/check puzzle' the given variables for the correct moves should now be true")
print("'given' variable for correct cell (1,1) should be true and for 2 incorrect cells (2,1), (0,3) should be false (formatted row, col, user entry, solution, is given/hardwired?)")
for ele in engine.history.history:
    print(ele.newCell.row,ele.newCell.col,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].GetEntry(),engine.puzzle.grid[ele.newCell.row][ele.newCell.col].solution,engine.puzzle.grid[ele.newCell.row][ele.newCell.col].given)

#now when undoing until correct, all wrong moves in history will be undone
#but user move of '4' in row 1 col 1 was right and checked as right so that should remain in the puzzle

undoneMoves = engine.UndoUntilCorrect()
#print("Undone moves addresses: ",undoneMoves)
for move in undoneMoves:
    print("UNDOING THIS MOVE AS PART OF UndoUntilCorrect() (formatted row,col,value)")
    print(move.oldCell.row,move.oldCell.col,move.newCell.GetEntry())
    engine.puzzle.SetCell(move.oldCell.row,move.oldCell.col,move.oldCell.GetEntry())
print()
print("PUZZLE BOARD WITH MOST RECENT STATUS OF WHEN FULL PUZZLE WAS CORRECT")
print_board(engine.puzzle.grid)

#RANDOM HINT

#MakeAMove(0,0,1)
MakeAMove(1,2,1)
MakeAMove(0,0,2)
MakeAMove(0,3,2)

print()
print("AFTER CALLING RANDOM HINT, THIS USER-ENTERED WRONG CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
#print(randHint[0]) #the row of hint cell ([1] would be column, [2] would be solution)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("CURRENT BOARD STATUS AFTER RANDOM HINT")
print_board(puzzleObj.grid)

print()
print("AFTER CALLING RANDOM HINT, THIS OTHER USER-ENTERED CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("CURRENT BOARD STATUS AFTER RANDOM HINT")
print_board(puzzleObj.grid)

print()
print("AFTER CALLING RANDOM HINT, THIS EMPTY CELL (row and col) AND SOLUTION VALUE ARE RETURNED")
randHint = engine.GetRandomHint()
print(randHint)
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print()
print("CURRENT BOARD STATUS AFTER RANDOM HINT")
print_board(puzzleObj.grid)

#SPECIFIC HINT

specHint = engine.GetSpecificHint(0,0)
print("CALLING SPECIFIC HINT OF USER-INPUTTED CORRECT BUT UNCHECKED CELL")
print(specHint) #should be None
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print()
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

#could not give a hint if ranodm hint randomly gave this cell's solution
specHint = engine.GetSpecificHint(0,2)
print("CALLING SPECIFIC HINT OF EMPTY CELL")
print(specHint) #should be None
print("LOOKING AT HISTORY STACK, MOST RECENT MOVE ON BOTTOM (last printed)")
print()
for ele in engine.history.history:
    print(ele.oldCell.row,ele.oldCell.col,ele.oldCell.GetEntry(),ele.newCell.row,ele.newCell.col,ele.newCell.GetEntry(),ele.isCorrect)

print("CURRENT BOARD STATUS AFTER SPECIFIC HINTS")
print_board(puzzleObj.grid)
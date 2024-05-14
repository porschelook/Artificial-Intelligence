from board import *
import time


def recursiveSimple(board):
    #Check to see a solution
    if board.toFill==0:
        return board, 0 #solution and number of backtracks
    #check to see if forwardCheck leads to 
    if not board.forwardCheck():
        #print("returning due to forward check")
        board.printBoard()
        return None, 0 #comunicate should backtrack
    #now select an index 
    fillX,fillY=board.emptyCells[0]
    #prepare for backtracking
    backup=board.copy()
    moveDomain=backup.cells[fillX][fillY].copy()
    runMoves=backup.copy()
    print(moveDomain)
    print(str(fillX) + ", "+str(fillY))
    backup.printBoard()
    backtracks=0
    #iterate through all the currently valid moves
    for move in moveDomain:
        if runMoves.fillCell(fillX,fillY,move)==-1:
            continue #make the move, skip if this move is not valid
        if runMoves.forwardCheck() ==False: #backtrack early
            runMoves=backup.copy()
            backtracks+=1
            continue
        solution, backs=recursiveSimple(runMoves)
        backtracks+=backs
        if solution is None:
            runMoves=backup.copy()
            backtracks+=1
            #print("backtracking")
        else:
            #solution.printBoard()
            #print("returning solution")
            return solution, backtracks
       
    print("ran through every solution")
    return None, 0
if __name__ == "__main__":

    b = board()
    b.printBoard()
    print("---------------------------")
    print(b.cells[0][0])
    print("forwardCheck ", b.forwardCheck())

    #f = open("../code_1/Sudoku/sudoku-problems.txt", "r")
    #test = f.readlines()

    #temp_board = []
    #all_board = []
    #for i in range(len(test)):

        #if i % 11 == 0 and i != 0:
            #all_board.append(temp_board)
            #temp_board = []
       # temp_board.append(test[i])
        #if i == len(test):
        #    all_board.append(temp_board)

    # for x in all_board:
      #  print(x)
    
    #s = open("../code_1/Sudoku/testExample.txt", "r")
    b.buildBoard("testExample.txt")
    b.printBoard()
    print(b.emptyCells)
    print(b.toFill)
    solvedBoard,backtracks=recursiveSimple(b)
    #print("solvedBoard ",solvedBoard.printBoard())
    solvedBoard.printBoard()
    print("backtracked number of times: " + str(backtracks))
#----------------------------------------------------

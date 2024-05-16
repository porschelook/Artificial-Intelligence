from board import *
import time


def recursiveSimple(board):
    # Check to see a solution
    if len(board.emptyCells) == 0:
        return board, 0  # solution and number of backtracks
    # check to see if forwardCheck leads to
    if not board.forwardCheck():
        #print("returning due to forward check")
        #board.printBoard()
        return None, 0  # comunicate should backtrack
    # do inference rules first
    board.propagateConstraints()
    if len(board.emptyCells) == 0:
        return board, 0  # solution and number of backtracks
    # now select an index
    fillX, fillY = board.emptyCells[0]
    # prepare for backtracking
    backup = board.copy()
    moveDomain = backup.cells[fillX][fillY].copy()
    runMoves = backup.copy()
    #print(moveDomain)
    #print(str(fillX) + ", " + str(fillY))
    #backup.printBoard()
    backtracks = 0
    # iterate through all the currently valid moves
    for move in moveDomain:
        if runMoves.fillCell(fillX, fillY, move) == -1:
            continue  # make the move, skip if this move is not valid
        if runMoves.forwardCheck() == False:  # backtrack early
            runMoves = backup.copy()
            backtracks += 1
            continue
        solution, backs = recursiveSimple(runMoves)
        backtracks += backs
        if solution is None:
            runMoves = backup.copy()
            backtracks += 1
            #print("backtracking")
        else:
            # solution.printBoard()
            #print("returning solution")
            return solution, backtracks

    #print("ran through every solution")
    return None, 0


def recursiveConstrained(board):
    # Check to see a solution
    if len(board.emptyCells) == 0:
        return board, 0  # solution and number of backtracks
    # check to see if forwardCheck leads to
    if not board.forwardCheck():
        # print("returning due to forward check")
        #board.printBoard()
        return None, 0  # comunicate should backtrack
    # do inference rules first
    board.propagateConstraints()
    if len(board.emptyCells) == 0:
        return board, 0  # solution and number of backtracks
    # now select an index
    fillX, fillY = board.mostConstrainedVariable()
    # prepare for backtracking
    backup = board.copy()
    moveDomain = backup.cells[fillX][fillY].copy()
    runMoves = backup.copy()
    #print(moveDomain)
    #print(str(fillX) + ", " + str(fillY))
    #backup.printBoard()
    backtracks = 0
    # iterate through all the currently valid moves
    for move in moveDomain:
        if runMoves.fillCell(fillX, fillY, move) == -1:
            continue  # make the move, skip if this move is not valid
        if runMoves.forwardCheck() == False:  # backtrack early
            runMoves = backup.copy()
            backtracks += 1
            continue
        solution, backs = recursiveConstrained(runMoves)
        backtracks += backs
        if solution is None:
            runMoves = backup.copy()
            backtracks += 1
            # print("backtracking")
        else:
            # solution.printBoard()
            # print("returning solution")
            return solution, backtracks

    print("ran through every solution")
    return None, 0


name = []
sudoku = []


def validBoardSeq(seq):
    if len(seq) != 81:
        return False
    validSet = [str(i) for i in range(10)]
    for i in seq:
        if i not in validSet:
            return False
    return True


def readAllpb():
    problemSet = []
    problemComments = []
    fname = "../code_1/Sudoku/sudoku-problems.txt"
    #fname = "sudoku-problems.txt"
    with open(fname, "r") as f:
        lines = [line.strip() for line in f]

    problem = ""
    for i, line in enumerate(lines):
        if i % 11 == 0:
            problemComments.append(line)
        elif i % 11 == 10:

            passOrnot = True
            if len(problem) != 81:
                passOrnot = False
            validSet = [str(i) for i in range(10)]
            for i in problem:
                if i not in validSet:
                    passOrnot = False
            passOrnot = True

            if not passOrnot:
                raise ValueError("Error")
            problemSet.append(problem)
            problem = ""
        else:
            problem += "".join(line.split())
    return (problemSet), (problemComments)


if __name__ == "__main__":

    b = board()
    b.printBoard()
    print("---------------------------")
    #print(b.cells[0][0])
    #print("forwardCheck ", b.forwardCheck())

    #b.buildBoard("../code_1/Sudoku/testExample.txt")

    #b.buildBoard("testExample.txt")
    #b.printBoard()
    #print(b.emptyCells)

    problemSet, problemComments = readAllpb()
    for i in range(30):
    #print(problemSet[0])
        print(problemComments[i])
        #print(problemSet[i])
        b = board()
        b.buildBoardString(problemSet[i])
        b.printBoard()
        print("-"*12)
        '''
        for x in problemSet:
        print(x)
        for x in problemComments:
        print(x)
        '''
        
        solvedBoard, backtracksConstrained = recursiveConstrained(b)
        _, backtracksSimple = recursiveSimple(b)
        # print("solvedBoard ",solvedBoard.printBoard())
        if solvedBoard == None:
            print("not found solution <<<<<<<<<<----------------------->>>>>>>>>>>>")
        else:
            solvedBoard.printBoard()
       
        print("backtracked number of times without heuristic: " + str(backtracksSimple))
        print("backtracked number of times with heuristic: " + str(backtracksConstrained))
    # ----------------------------------------------------

   

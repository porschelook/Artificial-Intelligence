from board import *
import time

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
    
    s = open("../code_1/Sudoku/testExample.txt", "r")
    b.buildBoard("../code_1/Sudoku/testExample.txt")
    b.printBoard()


    b.backtrackSearch()
from board import *

if __name__ == "__main__":
    initial_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 14, 15]] #
    b = state()
    print("board ", b.board[1])
    print("board ", b.board[3][1])

     

    print("manhattan distance", b.manh_dist())


    print("emptyLoc ",b.emptyLoc)
    print( b.board)
    b.moveLeft()

    print( b.board)
    print("emptyLoc ",b.emptyLoc)

    
    
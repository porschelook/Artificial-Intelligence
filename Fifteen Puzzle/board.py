import numpy as np
import random

class state:
    def __init__(self, board=None):
        #init into the solved state
        if board is None:
            temp=np.arange(15)+1#fifteen for the fifteen puzzle.
            temp=np.concatenate((temp,np.array([0])))#add in a zero for the empty cell
            self.board=np.reshape(temp,(4,4))# this is in row-major order so the first index is which row it is in and the second is which coilumn it is in.
        else:
            self.board=board.copy()#does a deep copy
            
        self.emptyLoc=(3,3)#initialize the spot of the empty square so it doesn't need to be searched for
        self.row=4
        self.col=4

    def scramble(self,numSteps):
        lastMove=None
        moves={"up", "right","left","down"}
        for i in range(numSteps):
            move=random.choice(tuple(moves-{lastMove}))
            #randomly choose a step that isn't the last one
            lastMove=move
            #apply move
            if move=="up":
                self.moveUp()
            if move=="right":
                self.moveRight()
            if move=="left":
                self.moveLeft()
            if move=="down":
                self.moveDown()    
    #changes the board state to that for which the empty (0) square has moved up one tile.         
    def moveUp(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=( max(0,self.emptyLoc[1]-1),self.emptyLoc[0])
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc

    def moveDown(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=( min(3,self.emptyLoc[1]+1),self.emptyLoc[0])
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc


    def moveLeft(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=(self.emptyLoc[0], max(0,self.emptyLoc[1]-1))
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc

    def moveRight(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=(self.emptyLoc[0], min(3,self.emptyLoc[1]+1))
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc

    def manh_dist(self):
        dist = 0
        for row in range(self.row):
            for col in range(self.col):

                if (value := self.board[row,col]) != 0:
                    print("v ",value)
                    value -= 1
                    x = value % self.col
                    y = value // self.row
                    dist += abs(x - col) + abs(y - row)
                    print("dist ",dist)

        return dist
    def copy(self):
        return state(board=self.board)

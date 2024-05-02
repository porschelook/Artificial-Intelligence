import numpy as np
import random
import time

GOAL = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


class state:
    emptyLoc =(3,3) 
    def __init__(self, board=None):
        # init into the solved state
        if board is None:
            temp = np.arange(15) + 1  # fifteen for the fifteen puzzle.
            temp = np.concatenate(
                (temp, np.array([0]))
            )  # add in a zero for the empty cell
             
            self.board = np.reshape(
                temp, (4, 4)
            )  # this is in row-major order so the first index is which row it is in and the second is which coilumn it is in.

        else:
            self.board = board.copy()  # does a deep copy

         # initialize the spot of the empty square so it doesn't need to be searched for
        self.row = 4
        self.col = 4

    def scramble(self, numSteps):
        lastMove = None
        moves = {"up", "right", "left", "down"}
        for i in range(numSteps):
            move = random.choice(tuple(moves - {lastMove}))
            # randomly choose a step that isn't the last one
            
            # apply move
            if move == "up":
                lastMove="down"
                self.moveUp()
            if move == "right":
                lastMove="left"
                self.moveRight()
            if move == "left":
                lastMove="right"
                self.moveLeft()
            if move == "down":
                lastMove="up"
                self.moveDown()

    # changes the board state to that for which the empty (0) square has moved up one tile.
    def moveUp(self):
        #print(self.emptyLoc)
        #print("self.board[self.emptyLoc] ",self.board[self.emptyLoc])
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=( max(0,self.emptyLoc[0]-1),self.emptyLoc[1])
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc

    def moveDown(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=( min(3,self.emptyLoc[0]+1),self.emptyLoc[1])
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc


    def moveLeft(self):
        assert self.board[self.emptyLoc] == 0
        newEmptyLoc = (self.emptyLoc[0], max(0, self.emptyLoc[1] - 1))
        self.board[newEmptyLoc], self.board[self.emptyLoc] = (
            self.board[self.emptyLoc],
            self.board[newEmptyLoc],
        )
        self.emptyLoc = newEmptyLoc
   

    def moveRight(self):
        assert self.board[self.emptyLoc]==0
        newEmptyLoc=(self.emptyLoc[0], min(3,self.emptyLoc[1]+1))
        self.board[newEmptyLoc], self.board[self.emptyLoc]=self.board[self.emptyLoc], self.board[newEmptyLoc]
        self.emptyLoc=newEmptyLoc

    def print_current_board(self):

        for i in self.board:
            for j in i:
                if j>0:
                    print(j, " ", end="")
                else:
                    print("  ", end="")
            print()

    def copy(self):
        newState = state(board=self.board)
        newState.emptyLoc = self.emptyLoc
        return newState

    def manh_dist(self):
        dist = 0
        for row in range(self.row):
            for col in range(self.col):
                if (value := self.board[row][col]) != 0:
                    #print("v ",value)
                    value -= 1
                    x = value % self.col
                    y = value // self.row
                    dist += abs(x - col) + abs(y - row)
                    #print("dist ",dist)
        return dist
    #To find an additional heuristic, I searched https://michael.kim/blog/puzzle
    def otherHeuristic(self):
        dist=self.manh_dist()
        temp=np.transpose(self.board)
        #count the number of horizontal conflicts
        horizCon=self.board[:,0:2]==(self.board[:,1:3]+1)
        dist+=2*np.sum(horizCon)
        #Do the same thing for vertical. Thisincludes the empty tile which shouldn't be counted.
        vertCon=temp[:,0:2]==(temp[:,1:3]+4)
        dist+=2*np.sum(vertCon)
        return dist
        
    
    def is_goal(self):
        if self.manh_dist() == 0:
            return True
        return False

    def check_can_move(self):
        cantmove = []
        if self.emptyLoc[0] == 0 :# can't up
            #print("can't up")
            cantmove.append("up")
        if self.emptyLoc[0] == 3 :# can't down
            #print("can't down")
            cantmove.append("down")
        if self.emptyLoc[1] == 0 :# can't left
            #print("can't left")
            cantmove.append("left")
        if self.emptyLoc[1] == 3 :# can't right
            #print("can't right")
            cantmove.append("right")
            
        return cantmove
    def __eq__(self,other):
        return np.array_equal(self.board,other.board)

class Node:
    def __init__(self, state, cost, heuristic, parent=None):
        self.state = state
        self.cost = cost
        self.heuristic = heuristic
        self.parent = parent
        self.f_score = cost + heuristic
    def __eq__(self,other):
        return self.state==other.state# and self.f_score==other.f_score#perhaps the new instance has a smaller cost.
    

def aStar(nodeState, funType="Other"):
    open_list = [Node(nodeState, 0, nodeState.manh_dist())]  # Start with the initial state
    closed_list = []
    totalHeuristic=0#keep running total of heuristic time
    while open_list:
        current_node = min(open_list, key=lambda x: x.f_score)
        
        current_node.state.check_can_move()
         
        open_list.remove(current_node)
        closed_list.append(current_node)
         
        if (
            current_node.heuristic == 0
        ):  # Define a method is_goal() to check if the state is the goal state
            return current_node, len(closed_list), totalHeuristic  # Return the goal node, number nodes expanded

        # Generate successor states and add them to the open list
        for move in ["up", "down", "left", "right"]:
            
            successor_state = current_node.state.copy()
              
            cannot_move = current_node.state.check_can_move()
            
            if move in cannot_move:
                 
                continue
             
            if move == "up":
                successor_state.moveUp()

            if move == "down":
                successor_state.moveDown()

            if move == "left":
                successor_state.moveLeft()

            if move == "right":
                successor_state.moveRight()
    

            #getattr(current_node.successor_state, f"move{move.capitalize()}")()  # Perform the move

            cost = current_node.cost + 1  # Assume uniform cost for each move
            heuristicTic=time.perf_counter()
            if funType=="other":
                heuristic =successor_state.otherHeuristic()#successor_state.manh_dist()
            else:
                heuristic=successor_state.manh_dist()
            heuristicToc=time.perf_counter()
            totalHeuristic+=heuristicToc-heuristicTic
            
            successor_node = Node(successor_state, cost, heuristic, current_node)
            if successor_node not in closed_list:#This would prefer a better equality
                open_list.append(successor_node)

                 

    return None  # No solution found

#TODO pass a list of what nodes the parrents have already seen so that cycles are reduced. 
def rbfs(node, f_limit,numVisited=0):
   
    if node.state.is_goal():
        return node, f_limit, numVisited

    successors = []
    for move in ["up", "down", "left", "right"]:
        if move not in node.state.check_can_move():
            successor_state = node.state.copy()
            getattr(successor_state, f"move{move.capitalize()}")()
            cost = node.cost + 1
            heuristic = successor_state.otherHeuristic()#manh_dist()
            numVisited+=1
            successor_node = Node(successor_state, cost, heuristic, node)
            '''if successor_node in closedNodes:
                if cost+heuristic<f_limit:
                    successors.append(successor_node)
            else:
                successors.append(successor_node)'''
            #somehow want to avoid re-hasing the same nodes
            successors.append(successor_node)

    if not successors:
        return None, np.inf, numVisited

    while True:
        successors.sort(key=lambda x: x.f_score)
        best = successors[0]
        if best.f_score > f_limit:
            return None, best.f_score, numVisited 
        alternative = successors[1].f_score if len(successors) > 1 else np.inf
        #closedNodes.append(best)
        result, best.f_score, numVisited = rbfs(best, min(f_limit, alternative),numVisited)
        if result is not None:
            return result, best.f_score, numVisited
        


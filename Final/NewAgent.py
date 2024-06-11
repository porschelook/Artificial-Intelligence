from environment import *
import itertools
Up, Down, Left, Right= range(4)

class BeliefNode:
    def __init__(self,env):
        #extract list of walls, build new architecture that captures belief states.
        #for now there are no walls
        self.beliefCells=[[{0,1} for cell in row] for row in env.rooms]
        self.current_x=env.current_x
        self.current_y=env.current_y
        self.currentFacing=Up
        
        self.scanDistance=env.scanDistance
        #for now, use fixed size
        self.scanDistance=2
    def __init__(self):
        #extract list of walls, build new architecture that captures belief states.
        #for now there are no walls
        self.beliefCells=[]
        self.current_x=0
        self.current_y=0
        self.currentFacing=Up
        
        #for now, use fixed size
        self.scanDistance=2
        #need to run an and-or plan
    #return a deep copy
    def copy(self):
        out=BeliefNode()
        out.beliefCells=self.beliefCells.copy()
        out.current_x=self.current_x
        out.current_y=self.current_y
        out.currentFacing= self.currentFacing
        out.scanDistance=self.scanDistance
        
               
    #This will return a set of states based on all posibilities of the scanning operation
    def scan(self):
       
        out=[]
        if self.currentFacine==Up:
            selectx=self.current_x
            starty=self.current_y
            endy=max(0,self.current_y-self.scanDistance)
            perms=itertools.product([0,1],repeat=starty-endy)
            for item in perms:
                additionalElement=self.copy()
                j=0
                for y in range(starty,endy, -1):
                    additionalElement.beliefCells[y][selectx]=item[j]
                    j+=1
                out.append(additionalItem)
            return out

class NewAgent(Agent):
    def __init__(self, env):# needs to generate the plan before it executes it
        self.beliefSpace=[BeliefNode(env)]
    def stepProgram(self,environment):
        # from simple agent **********************************************************
        
        #first, if the room is dirty, clean it
        if(not environment.getCurrentRoom().Isclean):
            environment.getCurrentRoom().Isclean=True
            environment.clean+=1
            return
        #Next, if the way forward is clear, move forward
        if(not environment.detectWall()):
            print(not environment.detectWall())
            environment.advance()
            return
        #If the way is blocked, turn right
        environment.turnRight()
    
 

from environment import *
import itertools
import copy
Up, Down, Left, Right= range(4)

class BeliefNode:
    def __init__(self,env=None):
        if env==None:
            
            #extract list of walls, build new architecture that captures belief states.
            #for now there are no walls
            self.beliefCells=[]
            self.current_x=0
            self.current_y=0
            self.currentFacing=Up
            #for now, use fixed size
            self.scanDistance=2
            self.height=0
            self.width=0
            #need to run an and-or plan
            return
        
        #extract list of walls, build new architecture that captures belief states.
        #for now there are no walls
        self.beliefCells=[[{0,1} for cell in row] for row in env.rooms]
        self.current_x=env.current_x
        self.current_y=env.current_y
        self.currentFacing=Up
        self.height=len(self.beliefCells)
        self.width=len(self.beliefCells[1])
        self.scanDistance=env.scanDistance
        #for now, use fixed size
        self.scanDistance=2
    #return a deep copy
    def copy(self):
        out=BeliefNode()
        out.beliefCells=copy.deepcopy(self.beliefCells)
        out.current_x=self.current_x
        out.current_y=self.current_y
        out.currentFacing= self.currentFacing
        out.scanDistance=self.scanDistance
        out.height=len(self.beliefCells)
        out.width=len(self.beliefCells[1])
        return out
        
               
    #This will return a set of states based on all posibilities of the scanning operation
    def scan(self):
        #TODO remove randomization from states already known
        out=[]
        if self.currentFacing==Up:
            selectx=self.current_x
            starty=self.current_y
            endy=max(0,self.current_y-self.scanDistance)
            perms=itertools.product([0,1],repeat=starty-endy)
            for item in perms:
                additionalElement=self.copy()
                j=0
                for y in range(starty,endy, -1):
                    #print(item[j])
                    #print(additionalElement.beliefCells[y][selectx])
                    if (additionalElement.beliefCells[y][selectx])=={1,0}:
                        additionalElement.beliefCells[y][selectx]=item[j]
                        
                    j+=1
                out.append(additionalElement)
            return out
        
        if self.currentFacing==Down:
            selectx=self.current_x
            starty=self.current_y
            endy=min(self.height,self.current_y+self.scanDistance)
            perms=itertools.product([0,1],repeat=starty-endy)
            for item in perms:
                additionalElement=self.copy()
                j=0
                for y in range(starty,endy, 1):
                    if (additionalElement.beliefCells[y][selectx])=={1,0}:
                        additionalElement.beliefCells[y][selectx]=item[j]
                    j+=1
                out.append(additionalElement)
            return out
        
        if self.currentFacing==Left:
            selecty=self.current_y
            startx=self.current_x
            endx=max(0,self.current_x-self.scanDistance)
            perms=itertools.product([0,1],repeat=startx-endx)
            for item in perms:
                additionalElement=self.copy()
                j=0
                for x in range(starty,endy, -1):
                    if (additionalElement.beliefCells[selecty][x])=={1,0}:
                        additionalElement.beliefCells[selecty][x]=item[j]
                    j+=1
                out.append(additionalElement)
            return out
        
        if self.currentFacing==Right:
            selecty=self.current_y
            startx=self.current_x
            endx=min(self.width,self.current_x+self.scanDistance)
            perms=itertools.product([0,1],repeat=startx-endx)
            for item in perms:
                additionalElement=self.copy()
                j=0
                for x in range(starty,endy, 1):
                    if (additionalElement.beliefCells[selecty][x])=={1,0}:
                        additionalElement.beliefCells[selecty][x]=item[j]
                    j+=1
                out.append(additionalElement)
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
    
 

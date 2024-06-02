from environment import *
Up, Down, Left, Right= range(4)

class NewAgent(Agent):
    def __init__(self, env):# needs to generate the plan before it executes it
        #extract list of walls, build new architecture that captures belief states.
        #for now there are no walls
        self.beliefCells=[[{0,1} for cell in row] for row in env.rooms]
        self.current_x=env.current_x
        self.current_y=env.current_y
        self.currentFacing=Up
        
        self.scanDistance=env.scanDistance
        #for now, use fixed size
        self.scanDistance=2
        #need to run an and-or plan
        
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
    
 

from environment import *


class NewAgent(Agent):
    def __init__(self, enviornment):# needs to generate the plan before it executes it
        #extract list of walls, build new architecture that captures belief states.
        
        
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
    
 

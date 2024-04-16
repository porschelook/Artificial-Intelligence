from environment import *
from random import randrange


class Agent:
    def stepProgram(self,environment):
        return

    
class RandomAgent(Agent):
    def stepProgram(self,environment):


        #first, if the room is dirty, clean it
        if(not environment.getCurrentRoom().Isclean):
            environment.getCurrentRoom().Isclean = True
            environment.clean += 1
            print("environment.getCurrentRoom()")
            return
        
        if randrange(2) == 1:
            if randrange(2) == 1:
                environment.turnRight()
                return
            else:
                environment.turnLeft()
                return

        if(not environment.detectWall()):
            environment.advance()
            return
        #If the way is blocked, random turn right or left
        if randrange(2) == 1:
            environment.turnRight()
        else:
            environment.turnLeft()
        
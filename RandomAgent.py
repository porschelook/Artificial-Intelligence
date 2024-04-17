from environment import *
from random import randrange
import random

RUN = 1
TURN = 0
RIGHT = 1
LEFT = 0
class Agent:
    def stepProgram(self,environment):
        return

  

 
 


class RandomAgent(Agent):
    def stepProgram(self,environment):
        #random turn or go foward with 30,60
        sampleList = [TURN, RUN]
        randomList = random.choices(sampleList, weights=(15,85), k=1)
        

        #first, if the room is dirty, clean it
        if(not environment.getCurrentRoom().Isclean):
            environment.getCurrentRoom().Isclean = True
            environment.clean += 1
            print("environment.getCurrentRoom()")
            return
        #random turn L R with 50,50
        turnList = [RIGHT, LEFT]
        randomTurnList = random.choices(turnList, weights=(50,50), k=1)
        
        if randomList[0] == TURN:
            if randomTurnList[0] == RIGHT:
                environment.turnRight()
                return
            else:
                environment.turnLeft()
                return

        if(not environment.detectWall()):
            environment.advance()
            return
        #If the way is blocked, random turn right or left
        if randomTurnList[0] == RIGHT:
            environment.turnRight()             
        else:
             environment.turnLeft()           
        
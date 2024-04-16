import sys
import random
from environment import *
from simpleAgent import *
from RandomAgent import *

NO_WALL = 0
WALL = 1

vacuum_model = None
model = int(input("Select Model: \n1 First_Model \n2 Second_Model \n3 Third_Model \n"))
match model:
    case 1:
        print("model_1")
        #set the model to run to be the memoryless deterministic agent
        vacuum_model=SimpleAgent()
    case 2:
        print("model_2")
        vacuum_model=RandomAgent()
        #set the model to be a random memoryless agent
    case 3:
        print("model_3")
        #set the model to be a small-memory agent
 

map = int(input("NoWall 1 \nWall 2\n"))

 
        
 
if map == 1:
    state = environment( NO_WALL)

    state.printCurrentWorld()

 
if map == 2:
    state = environment( WALL)
    state.printCurrentWorld()
 
#run a fixed number of steps. 500 should be good
for i in range(500):
    vacuum_model.stepProgram(state)
    #record relavent parameters for the report

    state.printCurrentWorld()
 

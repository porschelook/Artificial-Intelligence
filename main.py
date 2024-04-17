import sys
import random
from environment import *
from simpleAgent import *
from RandomAgent import *
from lowmemoryAgent import *
from threeBitAgent import *
import matplotlib.pyplot as plt
import numpy as np

NO_WALL = 0
WALL = 1

vacuum_model = None
model = int(input("Select Model: \n1 First_Model \n2 Second_Model \n3 Third_Model \n"))
numRuns=1
match model:
    case 1:
        print("model_1")
        #set the model to run to be the memoryless deterministic agent
        vacuum_model=SimpleAgent()
        numRuns=1
    case 2:
        print("model_2")
        vacuum_model=RandomAgent()
        numRuns=1
        #set the model to be a random memoryless agent
    case 3:
        print("model_3")
        vacuum_model=threeBitAgent()
        numRuns=1
        #set the model to be a small-memory agent
 

map = int(input("NoWall 1 \nWall 2\n"))

#run a fixed number of steps. 500 should be good
stop = 1e300#int(state.ROOM_DIMENSION*state.ROOM_DIMENSION*0.60)
cleanTrace=np.zeros(500)
        
for run in range(numRuns):
    #restart the enviornment after each run
    if map == 1:
        state = environment(NO_WALL)

        state.printCurrentWorld()

 
    if map == 2:
        state = environment(WALL)
        state.printCurrentWorld()
 


    for i in range(500):
        print(state.clean)
        cleanTrace[i]+=state.clean
        if state.clean >= stop:
            if state.detectHome():
                print("THISSSSSSS")
                break
        state.printCurrentWorld()
        vacuum_model.stepProgram(state)
    #record relavent parameters for the report

    #state.printCurrentWorld()
cleanTrace/=numRuns 
plt.plot(cleanTrace)
plt.xlabel("Number of steps")
plt.ylabel("Average number of clean tiles")
plt.show()

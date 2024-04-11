import sys
import random
from environment import *

NO_WALL = 0
WALL = 1

vacuum_model = None
model = int(input("Select Model: \n1 First_Model \n2 Second_Model \n3 Third_Model \n"))
match model:
    case 1:
        print("model_1")
    case 2:
        print("model_2")
    case 3:
        print("model_3")

 

map = int(input("NoWall 1 \nWall 2\n"))

 
        
 
if map == 1:
    state = environment( NO_WALL)
    state.printCurrentWorld()

 
if map == 2:
    state = environment( WALL)
    state.printCurrentWorld()
 

 
import os
import random
 
 

NO_WALL = 0
WALL = 1

class room:
        Isclean = 0
        IsDoor = 1
        name = ""
        def __init__(self, name):
            self.name = name
         
       


class environment:
    
    rooms = None
  
 
    p = 1
    INITIAL_X = 0
    INITIAL_Y = 0
    clean = 0
    current_x = 0
    current_y = 0
    Iswall = NO_WALL
   
    
    def __init__(self,wall):
        self.rooms = [[room(f"room {i}-{j}") for j in range(10)] for i in range(10)]
         
        self.INITIAL_X = 0 #start point
        self.INITIAL_Y = 9 #start point

        self.Total_clean = 0
        self.Total_action = 0

        self.current_x = self.INITIAL_X #start point
        self.current_y = self.INITIAL_Y #start point
        self.Iswall = wall

        if self.Iswall == WALL:
            for i in range(0, 10):
                for j in range(0, 10):
                    self.rooms[i][j].IsDoor  = 0 # set to wall
            #create Door set Door
            self.rooms[2][5].IsDoor = 1
            self.rooms[4][2].IsDoor = 1
            self.rooms[7][4].IsDoor = 1
            self.rooms[5][7].IsDoor = 1


    def printCurrentWorld(self):
       
        
        
        x = self.current_x
        y = self.current_y

        self.rooms[5][7].Isclean = 1 #test clean print
        if self.Iswall == WALL:
            print("--------------------------------")
            for i in range(0, 10):
                for j in range(0, 10):
                    if x == j and y == i:
                        print("R ", end="") 
                        continue
                    if self.rooms[i][j].Isclean == 0:
                        print("* ", end="")
                    else:
                        print("  ", end="")
                print("\n")

            print("--------------------------------")

        else:
            print("--------------------------------")
            for i in range(0, 10):
                for j in range(0, 10):
                    if x == j and y == i:
                        print("R ", end="") 
                        continue
                    if self.rooms[i][j].Isclean == 0:
                        print("* ", end="")
                    else:
                        print("  ", end="")
                print("\n")

            print("--------------------------------")

            
        
 

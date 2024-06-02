 
import os
import random
from random import randrange

 

NO_WALL = 0
WALL = 1

class Agent:
    def stepProgram(self,environment):
        return


class room:
        Isclean = 0
        IsDoor = 1
        
        name = ""
        def __init__(self, name):
            self.name = name
         
       

#define the room and the robot inside it. 
class environment:
    
    rooms = None
  
        
    p = 1
    INITIAL_X = 0
    INITIAL_Y = 0
    clean = 0
    current_x = 0
    current_y = 0
    Iswall = NO_WALL
    door1 = 4
    door2 = 6

    UP,RIGHT,DOWN,LEFT=range(4)#define directions robot can face in an order such that +1 is clockwise and -1 is counterclockwise
    INITIAL_DIRECTION=UP
    size_Board = 10 #default
    def __init__(self,wall,sizeBoard):
        self.scanDistance=5

        if sizeBoard > 0:
                print("new")   
                self.rooms = [[room(f"room {i}-{j}") for j in range(sizeBoard)] for i in range(sizeBoard)]  
                UP,RIGHT,DOWN,LEFT=range(4)#define directions robot can face
                self.INITIAL_X = 0 #start point
                self.INITIAL_Y = sizeBoard-1 #start point
                self.INITIAL_DIRECTION=UP
                self.ROOM_DIMENSION=sizeBoard
                self.Total_clean = 0
                self.Total_action = 0
                self.current_x = self.INITIAL_X #start point
                self.current_y = self.INITIAL_Y #start point
                self.current_direction=self.INITIAL_DIRECTION #start direction
                self.Iswall = wall
                wallPosition = int(self.ROOM_DIMENSION/2)
                self.size_Board =  sizeBoard
                print(self.ROOM_DIMENSION/2)
                if self.Iswall == WALL:
                
                        print("asdasd")
                        for i in range(0, self.ROOM_DIMENSION):
                                randX = random.randint(0, sizeBoard-1)
                                randY = random.randint(0, sizeBoard-1)
                                
                                # set Wall
                                self.rooms[randX][randY].IsDoor = 0
                                self.rooms[randY][randX].IsDoor = 0
                                # self.rooms[wallPosition][i].IsDoor = 0
                                # self.rooms[i][wallPosition].IsDoor = 0
                        # set Door
                        self.rooms[5][self.door1].IsDoor = 1
                        self.rooms[5][self.door2].IsDoor = 1
                        self.rooms[self.door1][5].IsDoor = 1
                        self.rooms[self.door2][5].IsDoor = 1


        else:
                print("default")   
                self.rooms = [[room(f"room {i}-{j}") for j in range(10)] for i in range(10)]
                UP,RIGHT,DOWN,LEFT=range(4)#define directions robot can face
                self.INITIAL_X = 0 #start point
                self.INITIAL_Y = 9 #start point
                self.INITIAL_DIRECTION=UP

                self.ROOM_DIMENSION=10
                self.Total_clean = 0
                self.Total_action = 0

                self.current_x = self.INITIAL_X #start point
                self.current_y = self.INITIAL_Y #start point
                self.current_direction=self.INITIAL_DIRECTION #start direction
                
                self.Iswall = wall

                wallPosition = int(self.ROOM_DIMENSION/2)
                print(self.ROOM_DIMENSION/2)
                if self.Iswall == WALL:
                
                        print("asdasd")
                        for i in range(0, self.ROOM_DIMENSION):
                                # set Wall
                                self.rooms[wallPosition][i].IsDoor = 0
                                self.rooms[i][wallPosition].IsDoor = 0
                        # set Door
                        
                        self.rooms[5][self.door1].IsDoor = 1
                        self.rooms[5][self.door2].IsDoor = 1
                        self.rooms[self.door1][5].IsDoor = 1
                        self.rooms[self.door2][5].IsDoor = 1
        
        self.printCurrentWorld()
    def scan(self):
        if self.current_direction == environment.UP:
            startIndex=self.current_y
            endIndex=max(0,self.current_y-self.scanDistance)
            scanList=[]
            for i in range(startIndex,endIndex,-1):
                scanList.append(self.rooms[i][self.current_x])
            return scanList
        if self.current_direction == environment.DOWN:
            startIndex=self.current_y
            endIndex=min(self.size_Board-1,self.current_y+self.scanDistance)
            scanList=[]
            for i in range(startIndex,endIndex,1):
                    scanList.append(self.rooms[i][self.current_x])
            return scanList
        if self.current_direction == environment.RIGHT:
            startIndex=self.current_x
            endIndex=min(self.sizeBoard-1,self.current_x+self.scanDistance)
            scanList=[]
            for i in range(startIndex,endIndex,1):
                scanList.append(self.rooms[self.current_y][i])
            return scanList

        if self.current_direction == environment.LEFT:
            startIndex=self.current_x
            endIndex=max(0,self.current_x-self.scanDistance)
            scanList=[]
            for i in range(startIndex,endIndex,-1):
                scanList.append(self.rooms[self.current_y][i])
            return scanList
                self.current_x-=1
        
        
    def advance(self):
            #moves based on stored orientation
        if self.current_direction == environment.UP:
                self.current_y-=1
        if self.current_direction == environment.DOWN:
                self.current_y+=1
        if self.current_direction == environment.RIGHT:
                self.current_x+=1
        if self.current_direction == environment.LEFT:
                self.current_x-=1
        #fix position to be within bounds
        self.current_y=max(0,self.current_y)
        self.current_x=max(0,self.current_x)        
        self.current_y=min(self.ROOM_DIMENSION,self.current_y)
        self.current_x=min(self.ROOM_DIMENSION,self.current_x)        
        #Next is to fix the robot from encountering a wall in the middle of the field
        return
    def turnLeft(self):
            #turn counter-clockwise
            self.current_direction=(self.current_direction-1)%4
    def turnRight(self):       
            #turn clockwise
            self.current_direction=(self.current_direction+1)%4
    def turnRandom(self):
            #turn counter-clockwise
            self.current_direction=(self.current_direction +randrange(4))%4
    def detectNextClean_mem(self):
        test_x=self.current_x
        test_y=self.current_y
        if self.current_direction == environment.UP:
                test_y=self.current_y-1
        if self.current_direction == environment.DOWN:
                test_y=self.current_y+1
        if self.current_direction == environment.RIGHT:
                test_x=self.current_x+1
        if self.current_direction == environment.LEFT:
                test_x=self.current_x-1
        if self.Iswall == WALL:
                
                if test_x == 5 :
                        if test_y != self.door1 or test_y != self.door2 :
                                return True
                        
                if test_y == 5 :
                        if test_x != self.door1 or test_x != self.door2:
                                return True      

        #This only works for the empty enviornment.
        
        if test_x<0 or test_y<0:
                return True
        if test_x>=self.size_Board or test_y>=self.size_Board:
                return True
        
         
        
        return False       
    def detectWall(self):
        test_x=self.current_x
        test_y=self.current_y
        if self.current_direction == environment.UP:
                test_y=self.current_y-1
        if self.current_direction == environment.DOWN:
                test_y=self.current_y+1
        if self.current_direction == environment.RIGHT:
                test_x=self.current_x+1
        if self.current_direction == environment.LEFT:
                test_x=self.current_x-1
        print("detectWall")
        print("test_x : " ,test_x)
        print("test_y : " ,test_y)
        if self.Iswall == WALL:
                if test_x == 5 :
                        if test_y != self.door1 and test_y != self.door2 :
                                return True
                        
                if test_y == 5 :
                        if test_x != self.door1 and test_x != self.door2:
                                return True      

      
        
        if test_x<0 or test_y<0:
                return True
        if test_x>=self.size_Board or test_y>=self.size_Board:
                return True
        
        
            
        return False
    def detectHome(self):
            return (self.current_x== 0 and self.current_y== 9)

    def getCurrentRoom(self):
            print("current_x ",self.current_x)
            print("current_y ",self.current_y)

            return self.rooms[self.current_y][self.current_x]
    def printCurrentWorld(self):
       
        
        
        x = self.current_x
        y = self.current_y

        #self.rooms[5][7].Isclean = 1 #test clean print
        if self.Iswall == WALL:
            print("--------------------------------")
            for i in range(0, self.size_Board):
                for j in range(0, self.size_Board):
                    if x == j and y == i:
                        print("R ", end="") 
                        continue
                    if self.rooms[i][j].IsDoor == False:
                        print("W ", end="")
                    else:
                        if self.rooms[i][j].Isclean == False:
                                print("* ", end="")
                        else:
                                print("  ", end="")
                print("\n")

            print("--------------------------------")

        else:
            print("--------------------------------")
            for i in range(0, self.size_Board):
                for j in range(0, self.size_Board):
                    if x == j and y == i:
                        print("R ", end="") 
                        continue
                    if self.rooms[i][j].IsDoor == False:
                        print("W ", end="")
                    else:
                          
                        if self.rooms[i][j].Isclean == False:
                                print("* ", end="")
                        else:
                                print("C ", end="")
                print("\n")

            print("--------------------------------")              
    

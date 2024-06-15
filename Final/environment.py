import os
import random
from random import randrange


NO_WALL = 0
WALL = 1
RANDOMWALL = 2


class Agent:
    def stepProgram(self, environment):
        return


class room:
    Isclean = 0
    IsDoor = 1

    name = ""

    def __init__(self, name):
        self.name = name
        self.Isclean = random.randrange(2) - 1


# define the room and the robot inside it.
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

    UP, RIGHT, DOWN, LEFT = range(
        4
    )  # define directions robot can face in an order such that +1 is clockwise and -1 is counterclockwise
    INITIAL_DIRECTION = UP
    size_Board = 10  # default

    countCell = 0
    # def CheckCanPassThroughAllCell(self,x,y):
    #         if self.countCell >= 3:
    #             return False
    #         if x < 0:
    #             self.countCell+=1
    #             return False
    #         if y < 0:
    #             self.countCell+=1
    #             return False
    #         if x >= self.size_Board:
    #             self.countCell+=1
    #             return False
    #         if y >= self.size_Board:
    #             self.countCell+=1
    #             return False

    #         if self.rooms[x][y+1].IsDoor == 0:
    #             self.countCell+=1
    #             CheckCanPassThroughAllCell(x,y+1)
    #         if self.rooms[x][y-1].IsDoor == 0:
    #             self.countCell+=1
    #             CheckCanPassThroughAllCell(x,y-1)

    #         if self.rooms[x+1][y].IsDoor == 0:
    #             self.countCell+=1
    #             CheckCanPassThroughAllCell(x+1,y)

    #         if self.rooms[x-1][y].IsDoor == 0:
    #             self.countCell+=1
    #             CheckCanPassThroughAllCell(x-1,y)

    #         return True
    def __init__(self, wall, sizeBoard):
        self.scanDistance = 2

        if sizeBoard > 0:
            # print("new")
            self.rooms = [
                [room(f"room {i}-{j}") for j in range(sizeBoard)]
                for i in range(sizeBoard)
            ]
            UP, RIGHT, DOWN, LEFT = range(4)  # define directions robot can face
            self.INITIAL_X = 0  # start point
            self.INITIAL_Y = sizeBoard - 1  # start point
            self.INITIAL_DIRECTION = UP
            self.ROOM_DIMENSION = sizeBoard
            self.Total_clean = 0
            self.Total_action = 0
            self.current_x = self.INITIAL_X  # start point
            self.current_y = self.INITIAL_Y  # start point
            self.current_direction = self.INITIAL_DIRECTION  # start direction
            self.Iswall = wall
            wallPosition = int(self.ROOM_DIMENSION / 2)
            self.size_Board = sizeBoard
            # print(self.ROOM_DIMENSION / 2)
            if self.Iswall == WALL:
                for i in range(0, self.ROOM_DIMENSION):
                    # set Wall
                    self.rooms[wallPosition][i].IsDoor = 0
                    self.rooms[i][wallPosition].IsDoor = 0
                    self.rooms[wallPosition][i].Isclean = 1
                    self.rooms[i][wallPosition].Isclean = 1
                # set Door
                self.rooms[wallPosition][wallPosition].IsDoor = 1
                self.rooms[wallPosition-1][wallPosition].IsDoor = 1
                self.rooms[wallPosition+1][wallPosition].IsDoor = 1
                self.rooms[wallPosition][wallPosition-1].IsDoor = 1
                self.rooms[wallPosition][wallPosition+1].IsDoor = 1

                self.rooms[wallPosition][wallPosition].Isclean = 1
                self.rooms[wallPosition-1][wallPosition].Isclean = 1
                self.rooms[wallPosition+1][wallPosition].Isclean = 1
                self.rooms[wallPosition][wallPosition-1].Isclean = 1
                self.rooms[wallPosition][wallPosition+1].Isclean = 1
 
            if self.Iswall == RANDOMWALL:
                for i in range(0, self.ROOM_DIMENSION + 10):
                    randX = random.randint(0, self.size_Board - 1)
                    randY = random.randint(0, self.size_Board - 1)

                    # print(CheckCanPassThroughAllCell(randX,randY))

                    # set Wall
                    self.rooms[randX][randY].IsDoor = 0
                    self.rooms[randX][randY].Isclean = 0
                    # self.rooms[randY][randX].IsDoor = 0
                    # self.rooms[wallPosition][i].IsDoor = 0
                    # self.rooms[i][wallPosition].IsDoor = 0
                # set Door
                self.rooms[self.ROOM_DIMENSION // 2][
                    self.ROOM_DIMENSION // 2 - 1
                ].IsDoor = 1
                self.rooms[self.ROOM_DIMENSION // 2][
                    self.ROOM_DIMENSION // 2 + 1
                ].IsDoor = 1
                self.rooms[self.ROOM_DIMENSION // 2 - 1][
                    self.ROOM_DIMENSION // 2
                ].IsDoor = 1
                self.rooms[self.ROOM_DIMENSION // 2 + 1][
                    self.ROOM_DIMENSION // 2
                ].IsDoor = 1
                self.rooms[self.INITIAL_X][
                    self.INITIAL_Y
                ].IsDoor = 1  # can not be the start position
                self.rooms[self.ROOM_DIMENSION // 2][
                    self.ROOM_DIMENSION // 2 - 1
                ].Isclean = 1
                self.rooms[self.ROOM_DIMENSION // 2][
                    self.ROOM_DIMENSION // 2 + 1
                ].Isclean = 1
                self.rooms[self.ROOM_DIMENSION // 2 - 1][
                    self.ROOM_DIMENSION // 2
                ].Isclean = 1
                self.rooms[self.ROOM_DIMENSION // 2 + 1][
                    self.ROOM_DIMENSION // 2
                ].Isclean = 1
                self.rooms[self.INITIAL_X][self.INITIAL_Y].Isclean = 1
        else:
            # print("default")
            self.rooms = [[room(f"room {i}-{j}") for j in range(10)] for i in range(10)]
            UP, RIGHT, DOWN, LEFT = range(4)  # define directions robot can face
            self.INITIAL_X = 0  # start point
            self.INITIAL_Y = 9  # start point
            self.INITIAL_DIRECTION = UP

            self.ROOM_DIMENSION = 10
            self.Total_clean = 0
            self.Total_action = 0

            self.current_x = self.INITIAL_X  # start point
            self.current_y = self.INITIAL_Y  # start point
            self.current_direction = self.INITIAL_DIRECTION  # start direction

            self.Iswall = wall
            self.size_Board = 10
            wallPosition = int(self.ROOM_DIMENSION / 2)
            # print(self.ROOM_DIMENSION / 2)
            if self.Iswall == WALL:
                for i in range(0, self.ROOM_DIMENSION):
                    # set Wall
                    self.rooms[wallPosition][i].IsDoor = 0
                    self.rooms[i][wallPosition].IsDoor = 0
                    self.rooms[wallPosition][i].Isclean = 1
                    self.rooms[i][wallPosition].Isclean = 1
                # set Door
                self.rooms[wallPosition][wallPosition-1].IsDoor = 1
                self.rooms[wallPosition][wallPosition+1].IsDoor = 1
                self.rooms[wallPosition-1][wallPosition].IsDoor = 1
                self.rooms[wallPosition+1][wallPosition].IsDoor = 1
                self.rooms[wallPosition][wallPosition-1].Isclean = 1
                self.rooms[wallPosition][wallPosition+1].Isclean = 1
                self.rooms[wallPosition-1][wallPosition].Isclean = 1
                self.rooms[wallPosition+1][wallPosition].Isclean = 1
            if self.Iswall == RANDOMWALL:
                for i in range(0, self.ROOM_DIMENSION + 10):
                    randX = random.randint(0, self.size_Board - 1)
                    randY = random.randint(0, self.size_Board - 1)

                    # set Wall
                    self.rooms[randX][randY].IsDoor = 0
                    self.rooms[randX][randY].Isclean = 1
                    # self.rooms[randY][randX].IsDoor = 0
                    # self.rooms[wallPosition][i].IsDoor = 0
                    # self.rooms[i][wallPosition].IsDoor = 0
                # set Door
                wallPosition = int(self.ROOM_DIMENSION / 2)
                self.rooms[wallPosition][wallPosition-1].IsDoor = 1
                self.rooms[wallPosition][wallPosition+1].IsDoor = 1
                self.rooms[wallPosition-1][wallPosition].IsDoor = 1
                self.rooms[wallPosition+1][wallPosition].IsDoor = 1
                self.rooms[wallPosition][wallPosition-1].Isclean = 1
                self.rooms[wallPosition][wallPosition+1].Isclean = 1
                self.rooms[wallPosition-1][wallPosition].Isclean = 1
                self.rooms[wallPosition+1][wallPosition].Isclean = 1
        # self.printCurrentWorld()

    def scan(self):
        if self.current_direction == environment.UP:
            startIndex = self.current_y
            endIndex = max(0, self.current_y - self.scanDistance)
            scanList = []
            for i in range(startIndex, endIndex, -1):
                scanList.append(self.rooms[i][self.current_x])
            return scanList
        if self.current_direction == environment.DOWN:
            startIndex = self.current_y
            endIndex = min(self.size_Board - 1, self.current_y + self.scanDistance)
            scanList = []
            for i in range(startIndex, endIndex, 1):
                scanList.append(self.rooms[i][self.current_x])
            return scanList
        if self.current_direction == environment.RIGHT:
            startIndex = self.current_x
            endIndex = min(self.sizeBoard - 1, self.current_x + self.scanDistance)
            scanList = []
            for i in range(startIndex, endIndex, 1):
                scanList.append(self.rooms[self.current_y][i])
            return scanList

        if self.current_direction == environment.LEFT:
            startIndex = self.current_x
            endIndex = max(0, self.current_x - self.scanDistance)
            scanList = []
            for i in range(startIndex, endIndex, -1):
                scanList.append(self.rooms[self.current_y][i])
            return scanList

    def advance(self):
        # moves based on stored orientation
        if self.current_direction == environment.UP:
            self.current_y -= 1
        if self.current_direction == environment.DOWN:
            self.current_y += 1
        if self.current_direction == environment.RIGHT:
            self.current_x += 1
        if self.current_direction == environment.LEFT:
            self.current_x -= 1
        # fix position to be within bounds
        self.current_y = max(0, self.current_y)
        self.current_x = max(0, self.current_x)
        self.current_y = min(self.ROOM_DIMENSION, self.current_y)
        self.current_x = min(self.ROOM_DIMENSION, self.current_x)
        # Next is to fix the robot from encountering a wall in the middle of the field
        return

    def turnLeft(self):
        # turn counter-clockwise
        self.current_direction = (self.current_direction - 1) % 4

    def turnRight(self):
        # turn clockwise
        self.current_direction = (self.current_direction + 1) % 4

    def turnRandom(self):
        # turn counter-clockwise
        self.current_direction = (self.current_direction + randrange(4)) % 4

    def detectNextClean_mem(self):
        test_x = self.current_x
        test_y = self.current_y
        if self.current_direction == environment.UP:
            test_y = self.current_y - 1
        if self.current_direction == environment.DOWN:
            test_y = self.current_y + 1
        if self.current_direction == environment.RIGHT:
            test_x = self.current_x + 1
        if self.current_direction == environment.LEFT:
            test_x = self.current_x - 1
        if self.Iswall == WALL:

            if test_x == 5:
                if test_y != self.door1 or test_y != self.door2:
                    return True

            if test_y == 5:
                if test_x != self.door1 or test_x != self.door2:
                    return True

        # This only works for the empty enviornment.

        if test_x < 0 or test_y < 0:
            return True
        if test_x >= self.size_Board or test_y >= self.size_Board:
            return True

        return False

    def detectWall(self):
        test_x = self.current_x
        test_y = self.current_y
        if self.current_direction == environment.UP:
            test_y = self.current_y - 1
        if self.current_direction == environment.DOWN:
            test_y = self.current_y + 1
        if self.current_direction == environment.RIGHT:
            test_x = self.current_x + 1
        if self.current_direction == environment.LEFT:
            test_x = self.current_x - 1
        # print("detectWall")
        # print("test_x : ", test_x)
        # print("test_y : ", test_y)
        if self.Iswall == RANDOMWALL:
            if (
                test_x < self.size_Board
                and test_y < self.size_Board
                and test_x >= 0
                and test_y >= 0
            ):
                # print(self.rooms[test_y][test_x].IsDoor)
                if self.rooms[test_y][test_x].IsDoor == 0:
                    # print("F_WALLLLLLLLL")
                    return True
            if test_x < 0 or test_y < 0:
                return True
            if test_x >= self.size_Board or test_y >= self.size_Board:
                return True

        if self.Iswall == WALL:

            if (
                test_x < self.size_Board
                and test_y < self.size_Board
                and test_x >= 0
                and test_y >= 0
            ):
                if self.rooms[test_y][test_x].IsDoor == 0:
                    # print("F_WALLLLLLLLL")
                    return True

        if test_x < 0 or test_y < 0:
            return True
        if test_x >= self.size_Board or test_y >= self.size_Board:
            return True

        return False

    def detectHome(self):
        return self.current_x == 0 and self.current_y == 9

    def getCurrentRoom(self):
        # print("current_x ", self.current_x)
        # print("current_y ", self.current_y)

        return self.rooms[self.current_y][self.current_x]
    def wallcreate(self):
        ans = [[0 for x in range(self.size_Board)] for y in range(self.size_Board)] # x = width, y = height
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

         
        x = self.current_x
        y = self.current_y

        # self.rooms[5][7].Isclean = 1 #test clean print
        
            
        for i in range(0, self.size_Board):
                for j in range(0, self.size_Board):
                    if x == j and y == i:
                        # print("R ", end="")
                        continue
                    if self.rooms[i][j].IsDoor == False:
                         
                        ans[i][j] = 1
                    else:
                        if self.rooms[i][j].Isclean == False:
                             
                            ans[i][j] = 0
                        else:
                            
                            ans[i][j] = 0
                 
         
     
        return ans
    def printCurrentWorld(self):

        x = self.current_x
        y = self.current_y

        # self.rooms[5][7].Isclean = 1 #test clean print
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
                            print("- ", end="")
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
                            print("- ", end="")
                print("\n")

            print("--------------------------------")


def scanDistanceANDcleanthatCELL(environment, distance):
    action = 0
    for _ in range(distance):
        if environment.detectWall():
            break
        current_room = environment.getCurrentRoom()
        if not current_room.Isclean:
            current_room.Isclean = True
            action = action +1
            # print(
            #     f"Cleaning room at ({environment.current_x}, {environment.current_y})"
            # )
        environment.advance()
        action = action +1
    # environment.printCurrentWorld()
     

    turnList = [0, 1,2,3]
    randomTurnList = random.choices(turnList, weights=(50, 50,50, 50), k=1)

    if randomTurnList[0] == 0:
        environment.turnRight()
        action = action +1
    elif randomTurnList[0] == 1: 
        environment.turnRight()
        action = action +1
        if not environment.detectWall():
            environment.advance()
            action = action +1
        environment.turnRight()
        action = action +1
    elif randomTurnList[0] == 2: 
        environment.turnLeft()
        action = action +1
        if not environment.detectWall():
            environment.advance()
            action = action +1
        environment.turnLeft()
        action = action +1
    else:
        environment.turnLeft()
        action = action +1
    return action 

def straightLineAlgorithm(environment,action):
    initial_direction = environment.current_direction
    scanDistance = 7
    
    while not all_cells_cleaned(environment):
        # environment.printCurrentWorld()
        current_room = environment.getCurrentRoom()
        if not current_room.Isclean:
            current_room.Isclean = True
            action = action + 1
            # print(
            #     f"Cleaning room at ({environment.current_x}, {environment.current_y})"
            # )
        acttionfromscandistacne = scanDistanceANDcleanthatCELL(environment, scanDistance)
        if environment.detectWall():
            if environment.current_direction == environment.RIGHT:
                environment.turnRight()
                action = action +1 
                if environment.detectWall():
                    environment.turnRight()
                    environment.turnRight()
                    action = action +2
            else:
                environment.turnLeft()
                action = action +1
                if environment.detectWall():
                    environment.turnLeft()
                    environment.turnLeft()
                    action = action +2
    
    return action+acttionfromscandistacne

def all_cells_cleaned(environment):
    # print("ALL :", all(room.Isclean for row in environment.rooms for room in row))
    return all(room.Isclean for row in environment.rooms for room in row)


# def main():
#     sizeBoard = 7
#     wall = NO_WALL
#     environment2 = environment(wall, sizeBoard)
#     print("Initial Environment:")
#     environment2.printCurrentWorld()

#     print("Running Straight Line Algorithm...")
#     straightLineAlgorithm(environment2)

#     print("Final Environment:")
#     environment2.printCurrentWorld()


# if __name__ == "__main__":
#     main()

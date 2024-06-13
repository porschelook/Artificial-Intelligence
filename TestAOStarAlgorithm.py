import os
import random
from random import randrange

NO_WALL = 0
WALL = 1
RANDOMWALL = 2

class Agent:
    def stepProgram(self, environment):
        return

class Room:
    def __init__(self, name):
        self.name = name
        self.Isclean = random.randrange(2) == 1
        self.IsDoor = True

class Environment:
    UP, RIGHT, DOWN, LEFT = range(4)  # Define directions
    INITIAL_DIRECTION = UP

    def __init__(self, wall, sizeBoard):
        self.scanDistance = 2

        self.rooms = [
            [Room(f"room {i}-{j}") for j in range(sizeBoard)]
            for i in range(sizeBoard)
        ]
        self.INITIAL_X = 0  # Start point
        self.INITIAL_Y = sizeBoard - 1  # Start point
        self.ROOM_DIMENSION = sizeBoard
        self.current_x = self.INITIAL_X  # Start point
        self.current_y = self.INITIAL_Y  # Start point
        self.current_direction = self.INITIAL_DIRECTION  # Start direction
        self.Iswall = wall
        wallPosition = int(self.ROOM_DIMENSION / 2)
        self.size_Board = sizeBoard

        if self.Iswall == WALL:
            for i in range(0, self.ROOM_DIMENSION):
                # Set Wall
                self.rooms[wallPosition][i].IsDoor = False
                self.rooms[i][wallPosition].IsDoor = False
            # Set Door
            self.rooms[5][4].IsDoor = True
            self.rooms[5][6].IsDoor = True
            self.rooms[4][5].IsDoor = True
            self.rooms[6][5].IsDoor = True
        elif self.Iswall == RANDOMWALL:
            for i in range(0, self.ROOM_DIMENSION + 10):
                randX = random.randint(0, self.size_Board - 1)
                randY = random.randint(0, self.size_Board - 1)
                self.rooms[randX][randY].IsDoor = False
            # Set Door
            self.rooms[self.ROOM_DIMENSION // 2][self.ROOM_DIMENSION // 2 - 1].IsDoor = True
            self.rooms[self.ROOM_DIMENSION // 2][self.ROOM_DIMENSION // 2 + 1].IsDoor = True
            self.rooms[self.ROOM_DIMENSION // 2 - 1][self.ROOM_DIMENSION // 2].IsDoor = True
            self.rooms[self.ROOM_DIMENSION // 2 + 1][self.ROOM_DIMENSION // 2].IsDoor = True
            self.rooms[self.INITIAL_X][self.INITIAL_Y].IsDoor = True  # Can not be the start position
        self.printCurrentWorld()

    def scan(self):
        scanList = []
        if self.current_direction == self.UP:
            for i in range(max(0, self.current_y - self.scanDistance), self.current_y):
                scanList.append(self.rooms[i][self.current_x])
        elif self.current_direction == self.DOWN:
            for i in range(self.current_y + 1, min(self.size_Board, self.current_y + self.scanDistance + 1)):
                scanList.append(self.rooms[i][self.current_x])
        elif self.current_direction == self.RIGHT:
            for i in range(self.current_x + 1, min(self.size_Board, self.current_x + self.scanDistance + 1)):
                scanList.append(self.rooms[self.current_y][i])
        elif self.current_direction == self.LEFT:
            for i in range(max(0, self.current_x - self.scanDistance), self.current_x):
                scanList.append(self.rooms[self.current_y][i])
        return scanList

    def advance(self):
        if self.current_direction == self.UP:
            self.current_y = max(0, self.current_y - 1)
        elif self.current_direction == self.DOWN:
            self.current_y = min(self.size_Board - 1, self.current_y + 1)
        elif self.current_direction == self.RIGHT:
            self.current_x = min(self.size_Board - 1, self.current_x + 1)
        elif self.current_direction == self.LEFT:
            self.current_x = max(0, self.current_x - 1)
        return

    def turnLeft(self):
        self.current_direction = (self.current_direction - 1) % 4

    def turnRight(self):
        self.current_direction = (self.current_direction + 1) % 4

    def turnRandom(self):
        self.current_direction = (self.current_direction + randrange(4)) % 4

    def detectWall(self):
        test_x, test_y = self.current_x, self.current_y
        if self.current_direction == self.UP:
            test_y -= 1
        elif self.current_direction == self.DOWN:
            test_y += 1
        elif self.current_direction == self.RIGHT:
            test_x += 1
        elif self.current_direction == self.LEFT:
            test_x -= 1

        if test_x < 0 or test_y < 0 or test_x >= self.size_Board or test_y >= self.size_Board:
            return True
        if self.Iswall == WALL:
            if (test_x == 5 and test_y not in {4, 6}) or (test_y == 5 and test_x not in {4, 6}):
                return True
        if self.Iswall == RANDOMWALL:
            if not self.rooms[test_y][test_x].IsDoor:
                return True
        return False

    def detectHome(self):
        return self.current_x == 0 and self.current_y == self.size_Board - 1

    def getCurrentRoom(self):
        return self.rooms[self.current_y][self.current_x]

    def printCurrentWorld(self):
        print("--------------------------------")
        for i in range(self.size_Board):
            for j in range(self.size_Board):
                if self.current_x == j and self.current_y == i:
                    print("R ", end="")
                elif not self.rooms[i][j].IsDoor:
                    print("W ", end="")
                else:
                    if not self.rooms[i][j].Isclean:
                        print("* ", end="")
                    else:
                        print("- ", end="")
            print("\n")
        print("--------------------------------")

# Node class for AO* algorithm
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.cost = 0  # Direct cost from parent to this node
        self.heuristic = self.calculate_heuristic()
        self.total_cost = self.cost + self.heuristic

    def calculate_heuristic(self):
        # Heuristic: number of dirty cells
        return number_of_dirty_cells(self.state)

    def is_goal(self):
        # Goal state: all cells are clean
        return all_cells_cleaned(self.state)

    def update_total_cost(self):
        self.total_cost = self.cost + self.heuristic

def AOStar(start_state):
    root = Node(start_state)
    open_list = [root]
    closed_list = []

    while open_list:
        current_node = select_most_promising_node(open_list)
        if current_node.is_goal():
            return extract_path(current_node)
        
        expand_node(current_node)

        # Add new nodes to open list
        for child in current_node.children:
            if child not in closed_list and child not in open_list:
                open_list.append(child)

        # Update costs and backtrack
        update_costs(current_node)
        closed_list.append(current_node)

def select_most_promising_node(open_list):
    # Select the node with the lowest total cost (heuristic + path cost)
    return min(open_list, key=lambda node: node.total_cost)

def expand_node(node):
    # Generate children nodes from the current node
    possible_moves = get_possible_moves(node.state)
    for move in possible_moves:
        new_state = apply_move(node.state, move)
        child_node = Node(new_state, node)
        child_node.cost = node.cost + move_cost(move)
        node.children.append(child_node)
        child_node.update_total_cost()

def update_costs(node):
    # Update costs from leaf to root
    if node.children:
        node.total_cost = min(child.total_cost for child in node.children)
    if node.parent:
        update_costs(node.parent)

def extract_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Helper functions
def number_of_dirty_cells(state):
    return sum(1 for row in state.rooms for cell in row if not cell.Isclean)

def all_cells_cleaned(state):
    return all(cell.Isclean for row in state.rooms for cell in row)

def get_possible_moves(state):
    # Possible moves: 'advance', 'turn_left', 'turn_right'
    return ['advance', 'turn_left', 'turn_right']

def apply_move(state, move):
    new_state = Environment(state.Iswall, state.size_Board)
    new_state.rooms = [[Room(f"room {i}-{j}") for j in range(state.size_Board)] for i in range(state.size_Board)]
    for i in range(state.size_Board):
        for j in range(state.size_Board):
            new_state.rooms[i][j].Isclean = state.rooms[i][j].Isclean
            new_state.rooms[i][j].IsDoor = state.rooms[i][j].IsDoor
    new_state.current_x = state.current_x
    new_state.current_y = state.current_y
    new_state.current_direction = state.current_direction

    if move == 'advance' and not new_state.detectWall():
        new_state.advance()
    elif move == 'turn_left':
        new_state.turnLeft()
    elif move == 'turn_right':
        new_state.turnRight()
    
    if new_state.getCurrentRoom().Isclean is False:
        new_state.getCurrentRoom().Isclean = True  # Clean the room

    return new_state

def move_cost(move):
    return 1  # Assume each move has a uniform cost for simplicity

def main():
    sizeBoard = 7
    wall = WALL
    start_environment = Environment(wall, sizeBoard)
    print("Initial Environment:")
    start_environment.printCurrentWorld()

    print("Running AO* Algorithm...")
    path = AOStar(start_environment)

    print("Path to clean all rooms:")
    for step in path:
        step.printCurrentWorld()

if __name__ == "__main__":
    main()

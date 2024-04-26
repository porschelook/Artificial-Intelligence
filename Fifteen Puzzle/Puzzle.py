class Puzzle:
    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0],
    ]  # 0 as empty or running factor
    current_state = [[], [], [], []]
    algo = ""
    zero_position = (3, 3)  # "0" zero position
    row = 4
    col = 4

    def __init__(self, algo, initial_state):
        self.algo = algo
        self.current_state = initial_state

    def set_empty_position(self, x, y):
        print("set new position ", x, " and ", y)
        self.zero_position = (x, y)

    def print_current_board(self):
        for i in self.current_state:
            for j in i:
                print(j, " ", end="")
            print()

    def move():
        print()

    def run(self):
        if self.algo == "A*":
            print("A*")
            self.do_astar()

        elif self.algo == "RBFS":
            print("RBFS")
            self.do_RBFS()
        else:
            print("None")

    # returns manhattan distance between board cells and their correctly indexes (skipping zero element)
    def manh_dist(self):
        dist = 0
        for row in range(self.row):
            for col in range(self.col):

                if (value := self.current_state[row][col]) != 0:
                    print("v ",value)
                    value -= 1
                    x = value % self.col
                    y = value // self.row
                    dist += abs(x - col) + abs(y - row)
                    print("dist ",dist)

        return dist

    def do_astar():
        print("do_astar")

    def do_RBFS():
        print("do_RBFS")




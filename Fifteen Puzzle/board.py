class Board:
    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0],
    ]  # 0 as empty or running factor
    current_state = [[], [], [], []]
    algo = ""
    empty_position = (3, 3)

    def __init__(self, algo):
        self.algo = algo

    def set_empty_position(self, x, y):
        print("set new position ",x ," and ", y)
        self.empty_position = (x,y)
       

    def print_current_board(self):

        for i in self.goal_state:
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

    def do_astar():
        print("do_astar")

    def do_RBFS():
        print("do_RBFS")


b = Board("A*")
print(b.algo)
print(b.empty_position)
b.set_empty_position(1,3)
print(b.empty_position)
b.print_current_board()

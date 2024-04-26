from Puzzle import *

if __name__ == "__main__":
    initial_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 14, 15]]
    b = Puzzle("A*", initial_state)
    print("algo ", b.algo)

    print("zero_position ", b.zero_position)
    b.print_current_board()

    print("manhattan distance", b.manh_dist())
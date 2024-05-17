
def load_puzzle(filename, level = "all"):
    level = level.capitalize()
    puzzles = []
    with open(filename, "r") as f:
        while(True):
            line = f.readline()
            if not line: break
            _, p_level = line.split(" ")
            p_level = p_level.rstrip("\n")
            if(p_level == level or level == "All"):
                puzzle = []
                for i in range(9):
                    puzzle_row = []
                    for digit in f.readline():
                        if digit not in ["\n", " "]:
                            puzzle_row.append(digit)
                    puzzle.append(puzzle_row)
                puzzles.append(puzzle)
            else:
                [f.readline() for _ in range(9)]
            f.readline()
    return  puzzles

def filled_counter(puzzle):
    filled_count = 0
    for row in puzzle:
        filled_count += (9 - row.count('0'))
    return filled_count

def print_puzzle(puzzle):
    for i,row in enumerate(puzzle):
        if(i % 3 == 0):
            print()
        print(" ".join(row[:3]) + "\t" + " ".join(row[3:6]) + "\t" + " ".join(row[6:]))

def data_logger(vpm = ["baseline", "mcv"], LEVELS = ["easy", "medium", "hard", "evil"]):
    data_log = {}
    for v in vpm:
        data_log[v] = {l:{"solved": 0, "time": [],"backtrack": [], "rules": None } for l in LEVELS}
    print(data_log)

    return data_log
# print_puzzle(load_puzzle("sudoku_problems.txt", level = "easy")[0])

data_logger()
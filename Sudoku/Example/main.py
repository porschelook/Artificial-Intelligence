from SudokuSolver import SudokuSolver
from utils import load_puzzle, filled_counter, data_logger
import sys

# 1: self.naked_singles
# 2: self.hidden_singles
# 3: self.naked_pairs
# 4: self.hidden_pairs
# 5: self.naked_triples
# 6: self.hidden_triples

LEVELS = ["easy", "medium", "hard", "evil"]
filled_averages = {}
data_log = data_logger()

def main():
    option, variable_select = menu()
    if(option == 1): 
        rules = [1, 2, 3, 4, 5, 6]
    elif(option == 2):
        rules = [1, 2]
    elif (option == 3):
        rules = [1, 2, 4]
    elif (option == 4):
        rules = [1, 2, 4, 6]
    elif(option == 5):
        rules = []
    if(variable_select == 1):
        variable_picking_approach = "baseline"
    else:
        variable_picking_approach = "mcv"
    
    filled_counts = []
    for level in LEVELS:
        for i, puzzle in enumerate(load_puzzle("sudoku_problems.txt", level = level)):
            print(level, i)
            filled_counts.append(filled_counter(puzzle))
            # solver = SudokuSolver(puzzle, variablePickingApproach = variable_picking_approach, rules = rules)
            # data = solver.solve()

            # data_log[variable_picking_approach][level]["solved"] += int(data["isSolved"])
            # if(data["isSolved"]):
            #     data_log[variable_picking_approach][level]["time"].append(data["time_taken"])
            #     data_log[variable_picking_approach][level]["backtrack"].append(data["btCount"])
            #     data_log[variable_picking_approach][level]["rules"] = rules
            
        filled_averages[level] = sum(filled_counts) / len(filled_counts)
    
    print(filled_averages)
        
def menu():
    print("Welcome to SuDoKu Solver\n")
    print("Choose the following options:")
    rules_select = int(input(
        '''
        Select the rules you want to apply:
        1. All
        2. Naked Singles and Hiddle singles
        3. Naked Singles, Hidden Singles and Pairs
        4. Naked Singles, Hidden Singles, Pairs and Triples
        5. No Inference
        6. Exit

        Your choice: '''))
    if(1 > rules_select or rules_select > 5):
        sys.exit()
    
    variable_select = int(input(
        '''
        Pick variable selection method:
        1. Baseline
        2. Most Constrained Variable

        Your choice: '''))
    if(variable_select not in [1, 2]):
        sys.exit()
    return rules_select, variable_select

main()
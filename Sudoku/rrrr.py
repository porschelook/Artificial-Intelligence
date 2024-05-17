import numpy as np

# Function to check if a number can be placed in a cell
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in board[:, col]:
        return False
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

# Function to get all possible candidates for each cell
def get_candidates(board):
    candidates = {}
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                candidates[(row, col)] = [num for num in range(1, 10) if is_valid(board, row, col, num)]
    return candidates

# Function to apply Naked Singles rule
def apply_naked_singles(board, candidates):
    for cell, nums in candidates.items():
        if len(nums) == 1:
            board[cell] = nums[0]
            print(" board[cell] ", board[cell])
            return True
    return False

# Function to apply Hidden Singles rule
def apply_hidden_singles(board, candidates):
    for unit in get_all_units():
        for num in range(1, 10):
            positions = [cell for cell in unit if num in candidates.get(cell, [])]
            if len(positions) == 1:
                board[positions[0]] = num
                return True
    return False

# Function to apply Naked Pairs rule
def apply_naked_pairs(board, candidates):
    for unit in get_all_units():
        pairs = [cell for cell in unit if len(candidates.get(cell, [])) == 2]
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                if set(candidates[pairs[i]]) == set(candidates[pairs[j]]):
                    for cell in unit:
                        if cell != pairs[i] and cell != pairs[j]:
                            for num in candidates[pairs[i]]:
                                if num in candidates.get(cell, []):
                                    candidates[cell].remove(num)
                                    return True
    return False

# Function to apply Hidden Pairs rule
def apply_hidden_pairs(board, candidates):
    for unit in get_all_units():
        for num1 in range(1, 10):
            for num2 in range(num1 + 1, 10):
                positions = [cell for cell in unit if num1 in candidates.get(cell, []) or num2 in candidates.get(cell, [])]
                if len(positions) == 2:
                    for cell in positions:
                        candidates[cell] = [num1, num2]
                    return True
    return False

# Function to apply Naked Triples rule
def apply_naked_triples(board, candidates):
    for unit in get_all_units():
        triples = [cell for cell in unit if len(candidates.get(cell, [])) in [2, 3]]
        for i in range(len(triples)):
            for j in range(i + 1, len(triples)):
                for k in range(j + 1, len(triples)):
                    combined = set(candidates[triples[i]] + candidates[triples[j]] + candidates[triples[k]])
                    if len(combined) == 3:
                        for cell in unit:
                            if cell != triples[i] and cell != triples[j] and cell != triples[k]:
                                for num in combined:
                                    if num in candidates.get(cell, []):
                                        candidates[cell].remove(num)
                                        return True
    return False

# Function to apply Hidden Triples rule
def apply_hidden_triples(board, candidates):
    for unit in get_all_units():
        for num1 in range(1, 10):
            for num2 in range(num1 + 1, 10):
                for num3 in range(num2 + 1, 10):
                    positions = [cell for cell in unit if num1 in candidates.get(cell, []) or num2 in candidates.get(cell, []) or num3 in candidates.get(cell, [])]
                    if len(positions) == 3:
                        for cell in positions:
                            candidates[cell] = [num for num in [num1, num2, num3] if num in candidates[cell]]
                        return True
    return False

# Function to get all units (rows, columns, and 3x3 boxes)
def get_all_units():
    units = []
    for i in range(9):
        units.append([(i, j) for j in range(9)])  # rows
        units.append([(j, i) for j in range(9)])  # columns
    for box_row in range(3):
        for box_col in range(3):
            units.append([(row, col) for row in range(box_row * 3, box_row * 3 + 3) for col in range(box_col * 3, box_col * 3 + 3)])
    return units

# Main solving function
def solve_sudoku(board):
    while True:
        candidates = get_candidates(board)
        if apply_naked_singles(board, candidates):
            continue
        if apply_hidden_singles(board, candidates):
            continue
        if apply_naked_pairs(board, candidates):
            continue
        if apply_hidden_pairs(board, candidates):
            continue
        if apply_naked_triples(board, candidates):
            continue
        if apply_hidden_triples(board, candidates):
            continue
        break

 

 
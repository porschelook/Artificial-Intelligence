import heapq

# Define movements
MOVEMENTS = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

class Grid:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start
        self.n = len(grid)
        self.total_cells_to_clean = sum(cell == 0 for row in grid for cell in row)

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.n and 0 <= y < self.n

    def is_obstacle(self, position):
        x, y = position
        return self.grid[x][y] == 1

    def get_neighbors(self, position):
        neighbors = []
        for move, (dx, dy) in MOVEMENTS.items():
            new_pos = (position[0] + dx, position[1] + dy)
            if self.is_within_bounds(new_pos) and not self.is_obstacle(new_pos):
                neighbors.append((new_pos, move))
        return neighbors

# Heuristic function
def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

# AO* Algorithm with backtracking to clean all cells
def ao_star_clean_all(grid_world):
    start = grid_world.start
    open_list = [(0, 0, start, [])]  # (f, g, current_position, path)
    closed_list = set()
    cleaned_cells = set([start])
    path = []
    actions = 0

    while open_list:
        f, g, current, current_path = heapq.heappop(open_list)
        
        if current in closed_list:
            continue
        
        current_path = current_path + [current]
        path.append(current)
        actions += 1

        if len(cleaned_cells) == grid_world.total_cells_to_clean:
            return path, actions
        
        closed_list.add(current)

        for neighbor, move in grid_world.get_neighbors(current):
            if neighbor not in cleaned_cells:
                cleaned_cells.add(neighbor)
                g_new = g + 1  # Assuming uniform cost for each move
                f_new = g_new + heuristic(neighbor, start)  # Heuristic updated to go back to start
                heapq.heappush(open_list, (f_new, g_new, neighbor, current_path))

        # Backtracking step
        if not any(neighbor not in closed_list for neighbor, _ in grid_world.get_neighbors(current)):
            path.pop()
            actions += 1  # Counting the backtracking step as an action
            if path:
                previous = path[-1]
                f_new = g + heuristic(previous, start)
                heapq.heappush(open_list, (f_new, g, previous, current_path[:-1]))

    return None, actions  # No path found

# Function to print the grid with the path
def print_map(grid, path):
    path_set = set(path)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in path_set:
                print("P", end=" ")
            elif grid[i][j] == 1:
                print("X", end=" ")
            else:
                print("0", end=" ")
        print()

# Example grid (0 = empty, 1 = obstacle)
grid = [
    [0, 0, 0, 0 ,0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
start = (0, 0)

# Create grid world and find the path to clean all cells
grid_world = Grid(grid, start)
path, actions = ao_star_clean_all(grid_world)

# Print the path on the grid and the number of actions
if path:
    print("Path found:")
    print_map(grid, path)
    print(f"Number of actions taken: {actions}")
else:
    print("No path found.")

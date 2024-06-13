import heapq

# Define movements and directions
DIRECTIONS = ["N", "E", "S", "W"]
MOVEMENTS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


class Grid:
    def __init__(self, grid, start):
        self.grid = grid
        self.start = start
        self.n = len(grid)
        self.total_cells_to_clean = sum(cell == 0 for row in grid for cell in row)
        self.belief_grid = [["?" for _ in range(self.n)] for _ in range(self.n)]
        self.belief_grid[start[0]][
            start[1]
        ] = "0"  # Starting position is known to be empty

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.n and 0 <= y < self.n

    def is_obstacle(self, position):
        x, y = position
        return self.grid[x][y] == 1

    def move(self, position, direction):
        dx, dy = MOVEMENTS[direction]
        new_pos = (position[0] + dx, position[1] + dy)
        if self.is_within_bounds(new_pos):
            if self.grid[new_pos[0]][new_pos[1]] == 1:
                self.belief_grid[new_pos[0]][
                    new_pos[1]
                ] = "X"  # Update belief grid with obstacle
            return new_pos
        return position

    def update_belief(self, position):
        x, y = position
        if self.grid[x][y] == 1:
            self.belief_grid[x][y] = "X"
        else:
            self.belief_grid[x][y] = "0"


# Heuristic function
def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


# AO* Algorithm with backtracking to clean all cells and maintain belief state
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

        grid_world.update_belief(current)

        if len(cleaned_cells) == grid_world.total_cells_to_clean:
            return path, actions

        closed_list.add(current)

        for direction in MOVEMENTS:
            next_pos = grid_world.move(current, direction)
            if next_pos != current and next_pos not in cleaned_cells:
                cleaned_cells.add(next_pos)
                g_new = g + 1
                f_new = g_new + heuristic(next_pos, start)
                heapq.heappush(open_list, (f_new, g_new, next_pos, current_path))

        # Backtracking step
        if not any(grid_world.move(current, d) not in closed_list for d in MOVEMENTS):
            path.pop()
            actions += 1  # Counting the backtracking step as an action
            if path:
                previous = path[-1]
                f_new = g + heuristic(previous, start)
                heapq.heappush(open_list, (f_new, g, previous, current_path[:-1]))

    return None, actions  # No path found


# Function to print the grid with the path and belief state
def print_map(grid, path, belief_grid):
    path_set = set(path)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in path_set:
                print("P", end=" ")
            elif belief_grid[i][j] == "X":
                print("X", end=" ")
            elif belief_grid[i][j] == "0":
                print("0", end=" ")
            else:
                print("?", end=" ")
        print()


# Example grid (0 = empty, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
]
start = (0, 0)

# Create grid world and find the path to clean all cells
grid_world = Grid(grid, start)
path, actions = ao_star_clean_all(grid_world)

# Print the path on the grid and the number of actions
if path:
    print("Path found:")
    print_map(grid, path, grid_world.belief_grid)
    print(f"Number of actions taken: {actions}")
else:
    print("No path found.")

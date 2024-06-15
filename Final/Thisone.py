
import heapq

class VacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.rows = len(environment)
        self.cols = len(environment[0])
        self.current_position = (0, 0)  # Starting position
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, Down, Right, Left
        self.num_actions = 0  # Counter for number of actions taken
    def is_valid_position(self, position):
        x, y = position
        return 0 <= x < self.rows and 0 <= y < self.cols and self.environment[x][y] != 'W'
    
    def cost(self, from_position, to_position):
        # Cost function: for simplicity, we use 1 for each move
        return 1
    
    def heuristic(self, position):
        # Heuristic function: Euclidean distance to the nearest D cell
        min_distance = float('inf')
        for i in range(self.rows):
            for j in range(self.cols):
                if self.environment[i][j] == 'D':
                    distance = ((position[0] - i) ** 2 + (position[1] - j) ** 2) ** 0.5
                    min_distance = min(min_distance, distance)
        return min_distance
    
    def ao_star_search(self):
        while self.has_dirty_cells():
            frontier = [(0, self.current_position)]  # (total_cost, position)
            heapq.heapify(frontier)
            explored = set()
            
            while frontier:
                total_cost, current_position = heapq.heappop(frontier)
                
                if current_position in explored:
                    continue
                
                explored.add(current_position)
                
                if self.environment[current_position[0]][current_position[1]] == 'D':
                    # Clean the current position
                    self.environment[current_position[0]][current_position[1]] = 'C'
                    # print(f"Cleaned position {current_position}")
                    self.num_actions += 1  # Increment action counter
                    # Continue searching for other D cells
                    break  # Exit the inner loop to re-evaluate the environment
                
                for action in self.actions:
                    new_position = (current_position[0] + action[0], current_position[1] + action[1])
                    
                    if self.is_valid_position(new_position):
                        new_cost = total_cost + self.cost(current_position, new_position)
                        priority = new_cost + self.heuristic(new_position)
                        heapq.heappush(frontier, (priority, new_position))
                        self.num_actions += 1  # Increment action counter

        print(f"Cleaning complete. Total actions taken: {self.num_actions}")
    
    def has_dirty_cells(self):
        # Check if there are any D cells left in the environment
        for i in range(self.rows):
            for j in range(self.cols):
                if self.environment[i][j] == 'D':
                    return True
        return False
# Example environment with walls
# D = Dirty, C = Clean, W = Wall
# environment_with_walls = [
#     ['C', 'D', 'W', 'C'],
#     ['C', 'W', 'C', 'D'],
#     ['D', 'D', 'C', 'D'],
#     ['C', 'C', 'W', 'C']
# ]

# agent_with_walls = VacuumAgent(environment_with_walls)
# agent_with_walls.ao_star_search()

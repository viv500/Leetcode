class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Convert obstacles to a set for quick lookup
        obstacles_set = set(map(tuple, obstacles))
        
        # Initial position and direction
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West
        
        # Maximum distance squared
        max_dist_sq = 0
        
        # Define direction vectors for North, East, South, West
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for move in commands:
            if move > 0:
                for _ in range(move):
                    next_x = x + direction_vectors[direction][0]
                    next_y = y + direction_vectors[direction][1]
                    
                    if (next_x, next_y) in obstacles_set:
                        break  # Stop moving in this direction
                    
                    # Update position
                    x, y = next_x, next_y
                    # Update maximum distance squared
                    max_dist_sq = max(max_dist_sq, x ** 2 + y ** 2)
            else:
                # Change direction
                if move == -2:
                    direction = (direction - 1) % 4
                elif move == -1:
                    direction = (direction + 1) % 4
        
        return max_dist_sq

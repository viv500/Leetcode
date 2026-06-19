from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = deque()
        fresh_orange_count = 0
        time = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                if grid[row][col] == 1:
                    fresh_orange_count += 1

        while rotten_oranges and fresh_orange_count:
            level_size = len(rotten_oranges)

            for _ in range(level_size):
                r, c = rotten_oranges.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_orange_count -= 1
                        rotten_oranges.append((nr, nc))
            
            time += 1

        
        return time if fresh_orange_count == 0 else -1


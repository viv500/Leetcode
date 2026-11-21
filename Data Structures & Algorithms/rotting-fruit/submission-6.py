from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1

                if grid[row][col] == 2:
                    rotten.append((row, col))
        
        time = 0
        while rotten and fresh_count > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        rotten.append((nr, nc))

            time += 1


        return time if fresh_count == 0 else -1

        
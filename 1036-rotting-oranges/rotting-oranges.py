from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs
        # need a for loop so we can increment counter level by level

        rows, cols = len(grid), len(grid[0])
        time = 0
        rotten = deque()
        fresh_orange_count = 0

        # collect all the rotten oranges so we can call bfs on them
        # O(n^2)
        for row in range(rows):
            for col in range(cols):
                # rotten orange!!
                if grid[row][col] == 2:
                    rotten.append((row, col))
                if grid[row][col] == 1:
                    fresh_orange_count += 1

        
        while(rotten and fresh_orange_count > 0):
            level_size = len(rotten)

            for _ in range(level_size):
                r, c = rotten.popleft()

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # mark rotten
                        rotten.append((nr, nc))
                        # 1 less fresh orange
                        fresh_orange_count -= 1
            time += 1

        return time if fresh_orange_count == 0 else -1

        return 


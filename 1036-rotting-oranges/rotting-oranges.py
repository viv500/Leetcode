from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rotten = deque()
        time = 0
        fresh_orange_count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_orange_count += 1
                if grid[row][col] == 2:
                    rotten.append((row, col))

        while rotten and fresh_orange_count > 0:
            level_size = len(rotten)

            for _ in range(level_size):
                r, c = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh_orange_count -= 1
                        rotten.append((nr, nc))
                        grid[nr][nc] = 0 # mark visited
            time += 1

        return -1 if fresh_orange_count != 0 else time


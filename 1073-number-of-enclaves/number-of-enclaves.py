from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        count = 0

        def dfs(r, c):
            if (r < 0 or
                c < 0 or
                r >= rows or
                c >= cols or grid[r][c] != 1):
                return

            grid[r][c] = 2

            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r + 1, c)

        for row in range(rows):
            if grid[row][0] == 1: dfs(row, 0)
            if grid[row][cols - 1] == 1: dfs(row, cols - 1)

        
        for col in range(cols):
            if grid[0][col] == 1: dfs(0, col)
            if grid[rows - 1][col] == 1: dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1

        return count
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.max_area = max(self.max_area, dfs(row, col))
                    grid[row][col] = 0

        return self.max_area
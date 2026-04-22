class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)

        return island_count            



            
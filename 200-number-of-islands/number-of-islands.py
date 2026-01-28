class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    dfs(row, col)

        return island_count


        
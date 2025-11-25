from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_area = 0

        def bfs(r, c):
            area = 1

            q = deque([(r, c)])
            grid[r][c] = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        area += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return area





        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, bfs(row, col))

        return max_area




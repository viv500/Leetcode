from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        q = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + row, dc + col

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # if it is found, it will no longer be visited again cuz it wont be INF
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))


from collections import deque
class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        distances = [[float("inf")] * cols for _ in range(rows)]
        distances[0][0] = 0

        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            if (r, c) == (rows - 1, cols - 1): return distances[r][c]


            weight = grid[r][c]

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    nei_weight = grid[nr][nc]

                    if distances[r][c] + nei_weight < distances[nr][nc]:
                        distances[nr][nc] = distances[r][c] + nei_weight
                        if nei_weight == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))

                
        
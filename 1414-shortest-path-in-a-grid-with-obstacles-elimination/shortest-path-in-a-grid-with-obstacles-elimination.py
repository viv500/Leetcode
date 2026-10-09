from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        q = deque([(0, 0, k, 0)])
        visited = set()
        visited.add((0, 0, k))
        steps = 0

        while q:
            r, c, k, steps = q.popleft()

            if (r, c) == (rows - 1, cols - 1): return steps

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 0 and (nr, nc, k) not in visited:
                        visited.add((nr, nc, k))
                        q.append((nr, nc, k, steps + 1))
                    elif grid[nr][nc] == 1 and k > 0 and (nr, nc, k - 1) not in visited:
                        visited.add((nr, nc, k - 1))
                        q.append((nr, nc, k - 1, steps + 1))

        return -1

        
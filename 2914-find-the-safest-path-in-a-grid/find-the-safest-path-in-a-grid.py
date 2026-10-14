from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols -1] == 1: return 0
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    q.append((row, col))

        while q:
            r, c = q.popleft()

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                grid[row][col] -= 1
        
        print(grid)

        maxHeap = [(-grid[0][0], 0, 0)]
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        visited = set((0, 0))

        while maxHeap:
            w, r, c = heapq.heappop(maxHeap)
            w = -w

            if (r, c) == (rows - 1, cols - 1):
                return w

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if min(w, grid[nr][nc]) < dist[nr][nc]:
                        visited.add((nr, nc))
                        dist[nr][nc] = min(w, grid[nr][nc])
                        heapq.heappush(maxHeap, (-(min(w, grid[nr][nc])), nr, nc))


        
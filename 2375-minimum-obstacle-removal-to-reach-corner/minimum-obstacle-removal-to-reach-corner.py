import heapq

class Solution:
    def minimumObstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        distances = [[float("inf")] * cols for _ in range(rows)]
        distances[0][0] = 0

        heap = [(0, 0, 0)]  # (distance, row, col)

        while heap:
            d, r, c = heapq.heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return d
            if d > distances[r][c]:
                continue  # stale entry, a shorter path was already found

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    nd = d + grid[nr][nc]
                    if nd < distances[nr][nc]:
                        distances[nr][nc] = nd
                        heapq.heappush(heap, (nd, nr, nc))
from collections import deque, defaultdict
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minCost = [[float("inf")] * cols for _ in range(rows)]
        minCost[0][0] = 0
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            cost, row, col = heapq.heappop(minHeap)

            if (row, col) == (rows - 1, cols - 1): return cost

            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = dr + row, dc + col

                if 0 <= nr < rows and 0 <= nc < cols:
                    temp = cost + grid[nr][nc]
                    if temp < minCost[nr][nc]:
                        minCost[nr][nc] = temp
                        heapq.heappush(minHeap, (temp, nr, nc))

        
        
import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float("inf") for _ in range(n)] for _ in range(n)] # this is distance from source to all nodes
        dist[0][0] = grid[0][0]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        minHeap = [(dist[0][0], (0, 0))]
        graph = defaultdict(list)

        print(dist)

        while minHeap:
            weight, coords = heapq.heappop(minHeap)
            r, c = coords

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and dist[r][c] + max(weight, grid[nr][nc]) < dist[nr][nc]:
                    dist[nr][nc] = max(weight, grid[nr][nc])
                    heapq.heappush(minHeap, (dist[nr][nc], (nr, nc)))

        
        return dist[n - 1][n - 1]

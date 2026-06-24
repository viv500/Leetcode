import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # edge weight = max in path so far
        rows, cols = len(grid), len(grid[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dist[0][0] = grid[0][0]

        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            weight, r, c = heapq.heappop(minHeap)

            if (r, c) == (rows - 1, cols - 1):
                return weight

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and max(dist[r][c], grid[nr][nc]) < dist[nr][nc]:
                    dist[nr][nc] = max(dist[r][c], grid[nr][nc])
                    heapq.heappush(minHeap, (dist[nr][nc], nr, nc))

        

            

import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        while minHeap:
            elevation, r, c = heapq.heappop(minHeap)

            if elevation > dist[r][c]: continue

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = max(elevation, grid[nr][nc])

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(minHeap, (new_cost, nr, nc))
                        
        return dist[rows - 1][cols - 1]
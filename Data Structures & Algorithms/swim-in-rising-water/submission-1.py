import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra variant: instead of summing edge weights, we track the
        # MAX elevation along a path (minimax path). The answer is the
        # smallest "max elevation" needed to reach the bottom-right cell.

        # djistra guarentees that the first time you pop from the minheap, that is the shortest path to that cell

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # distances[r][c] = min possible "max elevation" on any path from (0,0) to (r,c)
        distances = [[float("inf")] * cols for _ in range(rows)]
        distances[0][0] = grid[0][0]
        visited = set()

        # Heap entries: (max_elevation_on_path_so_far, row, col)
        minHeap = [(grid[0][0], 0, 0)]

        while minHeap:
            distance, row, col = heapq.heappop(minHeap)

            # Early exit: first time we pop the target, it's optimal (Dijkstra invariant)
            if (row, col) == (rows - 1, cols - 1):
                return distance

            # Skip stale heap entries (we may push the same cell multiple times)
            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                # Cost to step into neighbor = max of (path's current max, neighbor's elevation).
                # We don't need max(grid[row][col], grid[nr][nc]) because `distance` already
                # includes grid[row][col] from when (row,col) was relaxed.
                new_distance = max(distance, grid[nr][nc])

                # Standard relaxation: only update + push if we found a better path
                if new_distance < distances[nr][nc]:
                    distances[nr][nc] = new_distance
                    heapq.heappush(minHeap, (new_distance, nr, nc))
                    
        return distances[rows - 1][cols - 1]

# Time:  O(N^2 log N)  -- N^2 cells, each pushed at most a few times, log factor from heap
# Space: O(N^2)        -- distances grid, visited set, and heap
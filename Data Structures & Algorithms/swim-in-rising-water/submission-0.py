import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # djikstras problem where the "weight" is basically the cost of waiting which is the MAX elevation between 2 neighbouring cells
        # i.e. the time "t" it takes for a cell to be swimmable

        rows, cols = len(grid), len(grid[0])
        distances = [[float("inf")] * cols for _ in range(rows)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        minimum_time = float("inf")
        # base case
        distances[0][0] = 0

        minHeap = [(0, 0, 0)] # format (weight, row, col)



        while minHeap:
            distance, row, col = heapq.heappop(minHeap)

            if (row, col) in visited: 
                continue

            visited.add((row, col))

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
        
                if 0 <= nr < rows and 0 <= nc < cols:

                    time_needed = max(grid[row][col], grid[nr][nc])
                    new_distance = min(distances[nr][nc], max(distance, time_needed))
                    distances[nr][nc] = new_distance
                    heapq.heappush(minHeap, (new_distance, nr, nc))


        for distance in distances:
            print(distance)
        
        return distances[rows - 1][cols - 1]


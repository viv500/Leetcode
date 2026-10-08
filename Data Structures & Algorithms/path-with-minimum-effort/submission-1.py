from collections import defaultdict
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rows, cols = len(heights), len(heights[0])


        def generate_neis(r, c):
            result = []
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    result.append((nr, nc))

            return result


        minHeap = [(0, (0, 0))]
        dist = {}
        for row in range(rows):
            for col in range(cols):
                dist[(row, col)] = float("inf")

        dist[(0, 0)] = 0

        while minHeap:
            weight, (row, col) = heapq.heappop(minHeap)

            if (row, col) == (rows - 1, cols - 1): return weight

            neighbors = generate_neis(row, col)

            for r, c in neighbors:
                new_weight = max(dist[(row, col)],(abs(heights[r][c] - heights[row][col])))
                if new_weight < dist[(r, c)]:
                    dist[(r, c)] = new_weight
                    heapq.heappush(minHeap, (new_weight, (r, c)))

        
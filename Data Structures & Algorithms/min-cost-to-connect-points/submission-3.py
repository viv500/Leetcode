from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algoirthm
        minHeap = []
        visited = set()
        heapq.heappush(minHeap, (0, 0))
        cost = 0

        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    graph[i].append((distance, j))
        while minHeap and len(visited) < len(points):
            weight, node = heapq.heappop(minHeap)
            if node in visited: continue

            cost += weight
            visited.add(node)

            # expand frontier
            for weight, nei in graph[node]:
                heapq.heappush(minHeap, (weight, nei))

        return cost


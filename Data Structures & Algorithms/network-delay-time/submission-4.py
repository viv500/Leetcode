import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        distances = [float("inf")] * (n + 1)
        distances[0] = 0
        distances[k] = 0

        for u, v, t in times:
            graph[u].append([v, t])

        minHeap = [(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            for nei, nei_weight in graph[node]:
                if weight + nei_weight < distances[nei]:
                    distances[nei] = weight + nei_weight
                    heapq.heappush(minHeap, (distances[nei], nei))

        
        return max(distances) if max(distances) != float("inf") else -1


        
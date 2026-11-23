import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,t in times:
            graph[u].append((v, t))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        minHeap = [(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if weight > dist[node]: continue

            for nei, cost in graph[node]:
                new_cost = weight + cost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(minHeap, (new_cost, nei))

        dist = dist[1:]
        return max(dist) if max(dist) != float("inf") else -1


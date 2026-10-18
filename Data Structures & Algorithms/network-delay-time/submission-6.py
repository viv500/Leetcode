from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v, t))

        dist = [float("inf")] * (n + 1)
        visited = set()
        dist[k] = 0

        minHeap = [(0, k)]
        while minHeap:
            d, node = heapq.heappop(minHeap)
            visited.add(node)
            if d > dist[node]: continue

            for nei, nei_w in graph[node]:
                new_d = d + nei_w
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    heapq.heappush(minHeap, (new_d, nei)) 

        return max(dist[1:]) if max(dist[1:]) != float("inf") else -1

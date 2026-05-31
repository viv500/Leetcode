from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # minimum time it takes to reach all nodes = the max among minium times to reach all nodes
        graph = defaultdict(list)

        for u,v,time in times:
            graph[u].append((v, time))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        minHeap = [(0, k)]

        while minHeap:
            weight, node = heapq.heappop(minHeap)

            for nei, time in graph[node]:
                if weight + time < dist[nei]:
                    dist[nei] = weight + time
                    heapq.heappush(minHeap, (dist[nei], nei))

        ans = max(dist[1:])

        return -1 if ans == float("inf") else ans



        
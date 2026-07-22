from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))

        times = [float("inf")] * n
        times[k - 1] = 0
        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            for nei, cost in graph[node]:
                if cost + time < times[nei - 1]:
                    times[nei - 1] = cost + time
                    heapq.heappush(minHeap, (times[nei - 1], nei))

        return max(times) if max(times) != float("inf") else -1

        
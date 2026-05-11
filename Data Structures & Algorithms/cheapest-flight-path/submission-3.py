from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        best = {}                      # (node, stops) -> cost
        heap = [(0, src, 0)]           # (cost, node, stops)

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost
    
            best[(node, stops)] = cost

            for nei, nei_price in graph[node]:
                new_cost = cost + nei_price
                if (stops + 1 > k + 1) or new_cost >= best.get((nei, stops + 1), float("inf")):
                    continue
                heapq.heappush(heap, (new_cost, nei, stops + 1))

        return -1
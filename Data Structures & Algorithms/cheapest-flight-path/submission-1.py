from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # djikstras but with distance tracking (this is kinda like bfs + djikstras)

        # NOTE! in regular dijkstras, the first time you find a node, it is guarenteed to be the cheapest path there so
        # you add it to visited. here, that is not guarenteed and you may find a feasible solution later when the first solution wa
        # infeasible (too many stops)

        # NOTE! this is exaclty like djikstras but keeping track of distance and only adding back to heap if distance is feasible
        # we are guarenteed that the first time DST is popped, it is the minimum feasible cost

        # NOTE! you can stop pruning as soon as theres more than k stops! dont need to check

        # NOTE! best[(node, stops)] = cost . only continue pruning if you've found a cheaper path to a specific node with same number of steps!

        graph = defaultdict(list)
        best = {} # tracks (node, stops)] = cost
        for u, v, price in flights:
            graph[u].append((v, price))

        minHeap = [(0, src, 0)] # (price, node, distance from src)

        while minHeap:
            price, node, dist = heapq.heappop(minHeap)

            if node == dst:
                return price # guarenteed to be the minimum path

            best[(node, dist)] = price

            for nei, nei_price in graph[node]:
                if dist > k or best.get((nei, dist + 1), float('inf')) < price + nei_price: # only prune if same dest node with same number of stops is cheaper
                    # 1. if distance is feasible
                    # 2. if there no path to nei found before
                    # 1. if a previously found path to nei with same number of steps was more expensive than this path
                    continue
                heapq.heappush(minHeap, (price + nei_price, nei, dist + 1))

        
        return -1






        
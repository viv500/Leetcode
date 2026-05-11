from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 2 methods:
        # 1. Bellman ford time O( V * E), or this case O(V * k)
        # belman ford does the same source to all node task as djikstras but can handle negative edge weights unlike djikstras
        # here, it helps in a differner way for our extra constraint cuz belman ford involves v - 1 "relaxations"
        # but this is also a way to apply our constraint. the ith relaxation defines the minimum weight path from source to all edges in exactly i steps
        # so for us, its k iterations (since the src and dst are not included)

        distance = [float("inf") for _ in range(n)]
        distance[src] = 0 # distance to source is 0
        for _ in range(k + 1): # cuz number of stops doesn't include src or dst
            temp = distance.copy() # this is needed cuz we need to use the original distance values for all calculatinos within this iteration
            for u, v, cost in flights:
                
                temp[v] = min(temp[v], distance[u] + cost)

            distance = temp
            
        return -1 if distance[dst] == float("inf") else distance[dst]

        # 2. djikstras with modification: time O((V + E)log V)
        # doesnt work naturaly cuz dijkstras typically greedily picks min weight nodes and declares that as the min weight path to the. node
        # this doesnt work here cuz the "greedy" low weight path may lead to too many stops (infeasible)
        # so our visited set can't just be nodes, needs to be (nodes, number of steps)


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






        
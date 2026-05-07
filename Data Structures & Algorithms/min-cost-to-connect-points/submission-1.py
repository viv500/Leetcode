import heapq
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # "minimum cost to connect all points" -> MST
        # either PRIMS or KRUSKALS algoirthm
        # both are greedy MST algos. Prim better for dense Kruskal better for sparse
        # in this case, edges between all nodes are assumed to be present, so its a dense graph

        # use Prims!
        # 1. at each node, add all its neighbours and theri weights to min heap (frontier) IF the node it connects to
        #     hasn't been visited yet
        # 2. pop the node with the lowest weight from the min heap (the same node can have multiple entries with different weights in the minheap)
        # 3. add that to total and continue

        # note: need to store both node index and weight in min heap, in (weight, node) order so its sorted by weight

        minHeap = []
        visited = set()
        graph = defaultdict(list) # format: point index -> (distance, point index of neighbor)
        cost = 0

        heapq.heappush(minHeap, (0, 0)) # index 0 node is at a distance of 0, start with it

        # preprocessing graph (to optimize, calculate manhattan distance on the fly)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x_i, y_i = points[i]
                    x_j, y_j = points[j]
                    distance = abs(x_i - x_j) + abs(y_i - y_j)
                    graph[i].append((distance, j))

        while len(visited) < len(points):
            # pop the shortest distance
            distance, node = heapq.heappop(minHeap)
            if node in visited: continue
 
            cost += distance
            visited.add(node)

            # adding the frontier
            for distance, nei in graph[node]:
                if nei not in visited: heapq.heappush(minHeap, (distance, nei))

        return cost


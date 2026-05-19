from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Two approaches:

        # === 1. Bellman-Ford: O(k * E) ===
        # Bellman-Ford's i-th relaxation = min cost path using exactly i edges.
        # K stops = K+1 edges, so run K+1 iterations.
        # (would use >1 edge per round, breaking the invariant).

        # !! NOTE: using temp is not a part of Belman Ford but is needed in this algoirthm
        # to allow us to have the i-th iteration use exact i edges
        # temp -> helps prevent multi-hop propogation in 1 iterations

        # BUT, within 1 iteration, you can use newely discovered min values across different nodes

        distance = [float("inf")] * n
        distance[src] = 0

        for _ in range(k + 1):
            temp = distance.copy() # Need temp copy: prevents cascading updates within one iteration
            for u, v, cost in flights:
                temp[v] = min(temp[v], distance[u] + cost)
            distance = temp

        return distance[dst] if distance[dst] != float("inf") else -1

        # === 2. Modified Dijkstra: O((V + E) log V) ===
        # Standard Dijkstra fails: greedy min-cost path may exceed k stops.
        # Fix: track (node, stops) instead of just node.
        # First time dst pops = guaranteed min feasible cost.
        # Skip neighbor if: stops exceed k, OR cheaper path to (nei, stops+1) already found.

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
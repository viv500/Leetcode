from collections import defaultdict
import heapq

# Djikstras Algorithm: O(E log V)
# Using a minHeap -> Whenevr we pick the node with the shortest path from the queue, it is guarented
# that it is the shorest global path, and we can mark it visited
# result = max(result, path) is simplified to result = path since the paths are popped in ascending order anyway
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        visited = set()
        result = 0

        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        heapq.heapify(minHeap)

        while minHeap:
            path, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            result = path

            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (weight + path, neighbor))

        return result if len(visited) == n else -1


        
        
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Eulerian path (not circuit) problem.

        # Brute force: DFS with backtracking — O(E * E!), TLE
        # Better: Hierholzer's algorithm — O(E log E) due to sorting, O(E) space

        # Hierholzer's: greedily follow the smallest (alphabetical) destination at each node.
        # When stuck at a dead end, add it to the result and backtrack.
        # Reversing at the end gives the correct order since dead ends are last.

        # Sort in reverse so pop() yields the smallest (alphabetical) destination (pop is O(1) vs pop(0) O(n))
        # This is similar to topological sort — post-order append then reverse —
        # but works on edges instead of nodes and handles cycles.

        graph = defaultdict(list)
        output = []
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            output.append(node)

        dfs("JFK")
        return output[::-1]
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        components = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            neighbors = graph[node]

            if not neighbors: return

            for nei in neighbors:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        # note: dont iterate over graph. there could be nodes in range 0,n that have no edges, so they won't have graph entries
        for node in range(n):
            if node not in visited:
                visited.add(node)
                components += 1
                dfs(node)

        return components
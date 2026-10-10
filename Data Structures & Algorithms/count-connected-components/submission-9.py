from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        components = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                components += 1
                dfs(node)

        return components

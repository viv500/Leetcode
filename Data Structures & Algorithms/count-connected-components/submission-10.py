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
        for i in range(n):
            if i not in visited:
                visited.add(i)
                components += 1
                dfs(i)

        return components
        
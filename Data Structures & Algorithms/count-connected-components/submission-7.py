from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        component_count = 0
        visited = set()

        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in range(n):
            if node not in visited:
                dfs(node)
                component_count += 1
        
        return component_count

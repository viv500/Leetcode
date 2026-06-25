from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        component_count = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited: 
                    dfs(nei)

        
        for i in range(n):
            if i not in visited:
                component_count += 1
                dfs(i)

        return component_count

        
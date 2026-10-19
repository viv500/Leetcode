from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        if len(connections) < n - 1: return -1
        graph = defaultdict(list)
        visited = set()

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(computer):
            for nei in graph[computer]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        components = 0
        for computer in range(n):
            if computer not in visited:
                components += 1
                visited.add(computer)
                dfs(computer)

        return components - 1

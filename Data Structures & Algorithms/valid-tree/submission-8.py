from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        states = [0] * n

        def dfs(n, prev):
            if states[n] == 2: return True
            if states[n] == 1: return False

            states[n] = 1
            for nei in graph[n]:
                if nei != prev and not dfs(nei, n): return False
            states[n] = 2
            return True

        dfs(0, None)
        return sum(states) == 2 * len(states)
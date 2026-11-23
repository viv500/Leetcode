from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        states = [0] * n

        def dfs(prev, node):
            if states[node] == 1: return False
            if states[node] == 2: return True

            states[node] = 1
            for nei in graph[node]:
                if nei != prev and not dfs(node, nei): return False
            
            states[node] = 2
            return True


        no_cycles = dfs(-1, 0)
        connected = sum(states) == (2 * n)

        return no_cycles and connected
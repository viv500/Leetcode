from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree
        # 1. no cycles
        # 2. connected (not a forest) -> undirected edge is NOT a cycle so keep track of prev
        

        states = [0] * n
        graph = defaultdict(list)
        for u,v in edges:
            # undirected graph so both ways
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, prev):
            if states[node] == 1: return False
            if states[node] == 2: return True

            states[node] = 1
            for nei in graph[node]:
                if nei != prev and not dfs(nei, node): return False

            states[node] = 2
            return True

        # 1 dfs call works cuz it SHOULD visit all node in the tree
        # 1. no cycles
        if not dfs(0, -1): return False

        # 2. connected
        for state in states:
            if state == 0 : return False

        return True
        
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        def dfs(current, target, p, visited):
            if current == target: return p

            for nei, val in graph[current]:
                if nei not in visited:
                    visited.add(nei)
                    res = dfs(nei, target, p * val, visited)
                    if res != -1:
                        return res

            return -1

        result = []
            
        for a, b in queries:
            if a not in graph or b not in graph: result.append(-1)
            else: result.append(dfs(a, b, 1, {a}))

        return result




        
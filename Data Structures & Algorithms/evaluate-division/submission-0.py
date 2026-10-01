from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        output = []

        for index, (x, y) in enumerate(equations):
            graph[x].append((y, values[index]))
            graph[y].append((x, 1 / values[index]))


        def dfs(current, target, pdt):
            if current == target: return pdt

            for nei, val in graph[current]:
                if nei not in visited:
                    visited.add(nei)
                    result = dfs(nei, target, pdt * val)
                    if result != -1: return result

            return -1


        for x, y in queries:
            if x not in graph or y not in graph: 
                output.append(-1)
                continue
            visited = {x}
            output.append(dfs(x, y, 1))

        return output

        
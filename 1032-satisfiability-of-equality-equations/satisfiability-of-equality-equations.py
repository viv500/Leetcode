from collections import defaultdict
class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        graph = defaultdict(list)
        for eq in equations:
            a, op, _, b = eq
            if op == "=":
                graph[a].append(b)
                graph[b].append(a)

        def dfs(variable, target, visited):
            if variable == target: return True

            found = False
            for nei in graph[variable]:
                if nei not in visited:
                    visited.add(nei)
                    found = found or dfs(nei, target, visited)

            return found

        # checking inequalities
        for eq in equations:
            a, op, _, b = eq
            if op == "!" and dfs(a, b, set()): return False

        return True


        
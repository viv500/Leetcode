class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = [0]

        output = []

        def dfs(vertex):
            if vertex == len(graph) - 1:
                output.append(path.copy())
                return

            for nei in graph[vertex]:
                if nei not in path:
                    path.append(nei)
                    dfs(nei)
                    path.remove(nei)

        dfs(0)
        return output

        

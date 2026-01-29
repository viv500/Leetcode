class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colours = ['white'] * len(graph)

        def dfs(vertex):
            if colours[vertex] == 'white':
                colours[vertex] = 'red'

            complement = 'red' if colours[vertex] == 'blue' else 'blue'

            for nei in graph[vertex]:
                if colours[nei] == 'white':
                    colours[nei] = complement
                    if not dfs(nei): 
                        return False
                elif colours[nei] != complement:
                    return False
                else:
                    continue

            return True

        for vertex in range(len(graph)):
            if colours[vertex] == 'white':
                if not dfs(vertex): return False

        return True
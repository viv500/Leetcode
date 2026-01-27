class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 2 colouring algoirthm
        # if we encouter an already coloured node and its not the coloour we need
        # odd cycle ! since we started from a source node and ended on the same node too which
        # forms an odd length cycle <=> not bipartite

        # call dfs/bfs on every node if uncoloured. uncoloured means its on a separate component
        colour = ['white'] * len(graph)

        def dfs(node):
            if colour[node] == 'white':
                colour[node] = 'red'
            nei_colour = 'red' if colour[node] == 'blue' else 'blue'

            for nei in graph[node]:
                if colour[nei] == 'white':
                    colour[nei] = nei_colour
                    if not dfs(nei):
                        return False

                elif colour[nei] == nei_colour:
                    continue
                else:
                    print(node)
                    print(nei)
                    return False

            return True


        for node in range(len(graph)):
            if colour[node] == 'white':
                if not dfs(node): return False

        return True


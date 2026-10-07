class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        colours = ["white"] * len(graph)

        def dfs(node, prev_colour):
            opposite_colour = "red" if prev_colour == "blue" else "blue"

            if colours[node] == prev_colour: return False    
            elif colours[node] == opposite_colour: return True

            colours[node] = opposite_colour
            for nei in graph[node]:
                if not dfs(nei, colours[node]): return False

            return True


        for node in range(len(graph)):
            if colours[node] == "white" and not dfs(node, "red"): return False

        return True


        
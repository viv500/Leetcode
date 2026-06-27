from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        output = []
        min_height = float("inf")

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)
        
        def dfs_height(node):
            neis = []
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    neis.append(1 + dfs_height(nei))
             
            if not neis: return 0 # base case
            return max(neis)


        for i in range(n):
            # need to add root to visited set or it could be revisited
            visited = {i}
            height = dfs_height(i)
            if height < min_height:
                output = [i]
                min_height = height
            elif height == min_height:
                output.append(i)


        return output
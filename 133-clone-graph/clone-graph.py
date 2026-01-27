"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        # create hashmap that maps old vertices to new vertices
        # use this hashmap later to create connections
        mapping = {}

        # need a visited set cuz theres no way to mark visited
        visited = set()

        # crete reference to node so we dont lose it
        start = node

        # iterative dfs
        stack = [start]

        while stack:
            # i.e. popright
            vertex = stack.pop()
            mapping[vertex] = Node(vertex.val)

            for nei in vertex.neighbors:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        # create edges
        for old, new in mapping.items():
            for nei in old.neighbors:
                new.neighbors.append(mapping[nei])

        return mapping[start]

        # Time: O(V + E), Space: O(V) (hashmap and new graph)


        

            


        


        
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
        # also use to see if a node is visited
        mapping = {}

        # crete reference to node so we dont lose it
        start = node

        # iterative dfs
        stack = [start]
        mapping[start] = Node(start.val)

        while stack:
            # i.e. popright
            vertex = stack.pop()

            for nei in vertex.neighbors:
                if nei not in mapping:
                    stack.append(nei)
                    mapping[nei] = Node(nei.val)

        # create edges
        for old, new in mapping.items():
            for nei in old.neighbors:
                new.neighbors.append(mapping[nei])

        return mapping[start]

        # Time: O(V + E), Space: O(V) (hashmap and new graph)


        

            


        


        
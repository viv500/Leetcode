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
        mapping = {}

        start = node

        def dfs(node):
            if node in mapping: return
            mapping[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)

        dfs(node)

        for vertex, clone in mapping.items():
            for nei in vertex.neighbors:
                clone.neighbors.append(mapping[nei])

        return mapping[start]

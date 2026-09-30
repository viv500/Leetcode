"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        # first pass, creating the nodes
        visited = set()

        def dfs(node):
            if not node: return

            visited.add(node)
            old_to_new[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

            for nei in node.neighbors:
                old_to_new[node].neighbors.append(old_to_new[nei])

        dfs(node)

        return old_to_new[node] if node else node


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        root = node

        mapp = {}

        def dfs(node):
            new_node = Node(node.val)

            mapp[node] = new_node

            for nei in node.neighbors:
                if nei not in mapp: dfs(nei)

            for nei in node.neighbors:
                new_node.neighbors.append(mapp[nei])

        dfs(root)
        return mapp[root]

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        root = node
        visited = set()
        mapping = {node: Node(node.val)}

        q = deque([node])

        while q:
            node = q.popleft()

            for nei in node.neighbors:
                if nei.val not in visited:
                    visited.add(nei.val)
                    mapping[nei] = Node(val = nei.val)
                    q.append(nei)
                mapping[node].neighbors.append(mapping[nei])


        print(mapping)
        
        return mapping[root]

        
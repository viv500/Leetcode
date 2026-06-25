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
        root = node
        if not node: return None

        graph = {node: Node(node.val)}
        q = deque([node])

        while q:
            node = q.popleft()

            for nei in node.neighbors:
                if nei not in graph:
                    graph[nei] = Node(nei.val)
                    q.append(nei)

                graph[node].neighbors.append(graph[nei])

        
        return graph[root]


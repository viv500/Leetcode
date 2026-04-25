"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # problem: when creating new graph, difficuly to iterate when new nodes don't exist yet
        # first create all nodes and then create connections using an old-to-new-mapping

        # note: values are not guarenteed to be uniuqe, so just track the actual node
        if not node: return
        
        old_to_new = {}
        visited = set()
        cur = node

        stack = [node]
        old_to_new[node] = Node(val = node.val)
        while stack:
            node = stack.pop()

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

                    old_to_new[nei] = Node(val = nei.val)

        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[cur]
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
        if not node: return None

        old_to_new = {node: Node(val = node.val)}
        stack = [node]

        while stack:
            cur = stack.pop()

            for nei in cur.neighbors:
                if nei not in old_to_new:
                    stack.append(nei)
                    old_to_new[nei] = Node(val = nei.val)

                # neighbor guarenteed to be made, so add it
                old_to_new[cur].neighbors.append(old_to_new[nei])

        return old_to_new[node]
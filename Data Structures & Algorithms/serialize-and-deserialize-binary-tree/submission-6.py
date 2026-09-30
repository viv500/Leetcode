# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []

        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                tree.append("#")
                continue

            tree.append(str(node.val))
            
            q.append(node.left)
            q.append(node.right)

        return ",".join(tree)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "#": return None

        nodes = data.split(",")
        index = 0

        root = TreeNode(int(data[index]))

        q = deque([root])

        while q:
            node = q.popleft()

            index += 1
            node.left = TreeNode(int(nodes[index])) if nodes[index] != "#" else None
            if node.left: q.append(node.left)

            index += 1
            node.right = TreeNode(int(nodes[index])) if nodes[index] != "#" else None
            if node.right: q.append(node.right)
        
        return root
            


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
        path = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                path.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                path.append("#")

        return ",".join(path)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "#": return None

        data = data.split(",")
        idx = 0

        root = TreeNode(int(data[idx]))
        q = deque([root])
        while q:
            node = q.popleft()
            idx += 1

            if data[idx] != "#":
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            
            idx += 1

            if data[idx] != "#":
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)




        return root

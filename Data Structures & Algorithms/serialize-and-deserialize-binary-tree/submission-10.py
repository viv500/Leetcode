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
        code = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                code.append(str(node.val))
            else:
                code.append("#")
                continue

            q.append(node.left)
            q.append(node.right)

        return ",".join(code)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0] == "#": return None

        data = data.split(",")
        index = 0

        root = TreeNode(int(data[index]))
        q = deque([root])
        index += 1

        while q:
            node = q.popleft()
            if index < len(data) and data[index] != "#":
                node.left = TreeNode(int(data[index]))
                q.append(node.left)
            
            index += 1

            if index < len(data) and data[index] != "#":
                node.right = TreeNode(int(data[index]))
                q.append(node.right)
                
            index += 1

        return root



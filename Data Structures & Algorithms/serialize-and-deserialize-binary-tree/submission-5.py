# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# NOTE: dont use 2 * i + 1 and 2 * i + 2 logic: the in order traversal doesn't produce null children for null nodes in the string
#  tree [1,null,3,4,5,6,7] produces [1,null,3,6,7]
# ex. 1N34567NNNNNN is wrong, but 1N3NN45NNNN67NNNNNN is correct

# root=[1,null,3,4,5,6,7] would be null left child, 4 and 5 are 3's children, 6 and 7 are 3s children. no other nulls
# null doesn't have child nulls

from collections import deque


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using BFS."""
        code = ""
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                code += str(node.val) + "#"
                q.append(node.left)
                q.append(node.right)
            else:
                code += "N#"

        return code

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        tokens = [t for t in data.split("#") if t]

        if not tokens or tokens[0] == "N":
            return None

        root = TreeNode(val=int(tokens[0]))
        q = deque([root])
        i = 1

        while q and i < len(tokens):
            node = q.popleft()

            # Left child
            if tokens[i] != "N":
                node.left = TreeNode(val=int(tokens[i]))
                q.append(node.left)
            i += 1

            # Right child
            if i < len(tokens) and tokens[i] != "N":
                node.right = TreeNode(val=int(tokens[i]))
                q.append(node.right)
            i += 1

        return root
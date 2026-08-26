# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(node):
            if not node: return

            left = reverse(node.left)
            right = reverse(node.right)

            node.left, node.right = right, left

            return node

        return reverse(root)
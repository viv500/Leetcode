# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = root.val
        def dfs(node):
            if not node: return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.max_path = max(self.max_path, left + node.val + right)

            return node.val + max(left, right)

        dfs(root)

        return self.max_path
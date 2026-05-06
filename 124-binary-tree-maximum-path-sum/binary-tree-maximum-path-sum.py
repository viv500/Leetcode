# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(root):
            nonlocal max_path_sum
            if not root: return 0
            left_path = max(0, dfs(root.left))
            right_path = max(0, dfs(root.right))

            max_path_sum = max(max_path_sum, root.val + left_path + right_path)

            return max(root.val + left_path, root.val + right_path)

        dfs(root)

        return max_path_sum
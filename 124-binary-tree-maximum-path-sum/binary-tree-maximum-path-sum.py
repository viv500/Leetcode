# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf") # there can be negative paths

        def dfs(node):
            nonlocal max_path
            if not node: return 0

            max_left_path = max(0, dfs(node.left)) #helps avoid negative weight paths
            max_right_path = max(0, dfs(node.right))

            max_path = max(max_path, max_left_path + node.val + max_right_path)

            return node.val + max(max_left_path, max_right_path)

        dfs(root)

        return max_path

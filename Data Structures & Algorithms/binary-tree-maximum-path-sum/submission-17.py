# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def bfs(node):
            if not node: return 0

            nonlocal max_path

            left_max = max(0, bfs(node.left))
            right_max = max(0, bfs(node.right))

            max_path = max(max_path, left_max + node.val + right_max)

            return node.val + max(left_max, right_max)

        bfs(root)
        return max_path
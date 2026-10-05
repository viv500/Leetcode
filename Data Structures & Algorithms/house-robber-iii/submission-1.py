# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        dp = {}

        def dfs(node, prev_stole):
            if not node: return 0

            if (node, prev_stole) in dp: return dp[(node, prev_stole)]

            steal = 0
            if not prev_stole:
                steal = node.val + dfs(node.left, True) + dfs(node.right, True)
            skip = dfs(node.left, False) + dfs(node.right, False)

            dp[(node, prev_stole)] = max(steal, skip)
            return  dp[(node, prev_stole)]

        return dfs(root, False)
            
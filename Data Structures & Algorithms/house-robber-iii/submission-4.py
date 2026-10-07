# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def dfs(node, prev_taken):
            if not node: return 0
            if (node, prev_taken) in dp: return dp[(node, prev_taken)]

            skip = dfs(node.left, False) + dfs(node.right, False)
            if prev_taken: return skip

            take = node.val + dfs(node.left, True) + dfs(node.right, True)
            dp[(node, prev_taken)] = max(skip, take)
            return dp[(node, prev_taken)]

        return dfs(root, False)
                
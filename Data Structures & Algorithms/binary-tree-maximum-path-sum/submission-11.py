# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # brute force: for each node, calculate:
        # longest path sum on left + node.val + longest path sum on right
        # a lot of repeated calculations

        # better approach that's O(n) time and O(log n) space
        result = float('-inf')

        def dfs(node):
            nonlocal result
            if not node: return 0

            # path can zigzag, a right path will also reach this left path statement in dfs
            left_sum = max(0, dfs(node.left)) # handles case where child sum is negative
            right_sum = max(0, dfs(node.right))

            result = max(result, node.val, node.val + left_sum + right_sum)
            # result assuming current node is the only "branch split"

            return max(node.val, node.val + left_sum, node.val + right_sum)
            # return to parent caller assuming current node is not the "branch split"
            # i.e. return max straight path

        dfs(root)

        return result

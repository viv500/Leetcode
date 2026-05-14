# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force: exploring left and right sub trees for each node, loads of repeated work!
        # O(n^2)

        # dfs approach: running a dfs that returns info about if the node was balances, along with the max height between
        # left and right subtree

        def dfs(root):
            if not root: return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        
        return dfs(root)[0]
            
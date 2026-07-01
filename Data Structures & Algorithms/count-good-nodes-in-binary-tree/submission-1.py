# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        def dfs(root, maxInPath):
            if not root: return

            if root.val >= maxInPath: self.goodNodes += 1
            maxInPath = max(maxInPath, root.val)

            dfs(root.left, maxInPath)
            dfs(root.right, maxInPath)

        dfs(root, float("-inf"))

        return self.goodNodes
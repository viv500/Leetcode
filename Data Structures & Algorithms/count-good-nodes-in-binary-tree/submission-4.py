# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, highest):
            if not node: return

            if node.val >= highest: self.count += 1

            highest = max(highest, node.val)

            dfs(node.left, highest)
            dfs(node.right, highest)

        dfs(root, float("-inf"))

        return self.count
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is ALWAYS a good node
        goodNodeCount = 0

        def explore(node, maxInPath):
            nonlocal goodNodeCount
            if not node:
                return

            if node.val >= maxInPath:
                maxInPath = max(maxInPath, node.val)
                goodNodeCount += 1

            explore(node.left, maxInPath)
            explore(node.right, maxInPath)

        explore(root, float("-inf"))

        return goodNodeCount

        
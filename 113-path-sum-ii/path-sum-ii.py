# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []
        path = []
        def backtrack(node, targetSum):
            if not node: return

            targetSum -= node.val
            path.append(node.val)

            if not node.left and not node.right and targetSum == 0:
                result.append(path[:])

            for child in (node.left, node.right):
                backtrack(child, targetSum)

            path.pop()

        backtrack(root, targetSum)
        return result
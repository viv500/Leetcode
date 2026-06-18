# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validTree(root, low, high):
            if not root: return True
            if root.val >= high or root.val <= low: return False

            return validTree(root.left, low, root.val) and validTree(root.right, root.val, high)

        return validTree(root, float("-inf"), float("inf"))

            
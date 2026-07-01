# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, left, right):
            if not node: return True
            isValidNode = left < node.val < right

            return isValidNode and validate(node.left, left, node.val) and validate(node.right, node.val, right)


        return validate(root, float("-inf"), float("inf"))
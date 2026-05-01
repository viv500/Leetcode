# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # important ! need to pass down updated boundaries to descendants
    # left child inherits parent's left limit but parent val is ITS right limit
    # right child inherits parent's right limit but parent val is ITS left limit
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isInRange(root, left_limit, right_limit):
            if not root: return True

            if root.val >= right_limit or root.val <= left_limit: return False

            return isInRange(root.left, left_limit, root.val) and isInRange(root.right, root.val, right_limit)


        return isInRange(root, float('-inf'), float('inf'))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # format: [height, isBalanced]

        def balanced(node):
            if not node: return [0, True]

            left_height, left_is_balanced = balanced(node.left)
            right_height, right_is_balanced = balanced(node.right)

            isbalanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)

            return [height, isbalanced]



        return balanced(root)[1]
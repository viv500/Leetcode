# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced(root):
            if not root:
                return [True, 0]

            left_balanced, left_subtree = balanced(root.left)
            right_balanced, right_subtree = balanced(root.right)

            return [left_balanced and right_balanced and abs(left_subtree - right_subtree) <= 1, 1 + max(left_subtree, right_subtree)]

        return balanced(root)[0]
                


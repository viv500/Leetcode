# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float("-inf")

        def dfs(node):
            nonlocal diameter
            if not node: return 0

            left_child = 1 + dfs(node.left)
            right_child = 1 + dfs(node.right)

            diameter = max(diameter, left_child + right_child - 2)

            return max(left_child, right_child)

        
        dfs(root)

        return diameter
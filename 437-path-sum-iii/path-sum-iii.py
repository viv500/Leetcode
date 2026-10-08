# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.total_count = 0

        def dfs(node):
            if not node: return

            self.total_count += count_target_paths(node, targetSum)

            dfs(node.left)
            dfs(node.right)

        def count_target_paths(root, targetSum):
            if not root: return 0

            targetSum -= root.val
            children = count_target_paths(root.left, targetSum) + count_target_paths(root.right, targetSum)
            return 1 + children if targetSum == 0 else children

        dfs(root)
        return self.total_count






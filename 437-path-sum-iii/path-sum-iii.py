# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        self.target_count = 0
        self.current_count = 0

        def dfs(node):
            if not node: return

            self.current_count += node.val

            prefix = self.current_count - targetSum
            if prefix in prefix_count:
                self.target_count += prefix_count[prefix]

            prefix_count[self.current_count] += 1

            dfs(node.left)
            dfs(node.right)

            prefix_count[self.current_count] -= 1
            self.current_count -= node.val

        dfs(root)
        return self.target_count








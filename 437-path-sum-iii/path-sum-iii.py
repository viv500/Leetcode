# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# brute force O(n^2), prefix sums are O(n)
# if we pass cur sum as a parameter, dont need to undo cuz were only decremenenting local copy
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        self.target_count = 0

        def dfs(node, curSum):
            if not node: return

            curSum += node.val
            self.target_count += prefix_count[curSum - targetSum]

            prefix_count[curSum] += 1

            dfs(node.left, curSum)
            dfs(node.right, curSum)

            prefix_count[curSum] -= 1


        dfs(root, 0)
        return self.target_count








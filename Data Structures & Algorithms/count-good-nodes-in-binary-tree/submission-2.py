# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_node_count = 0

        def dfs(node, greatest):
            if not node: return

            if node.val >= greatest:
                self.good_node_count += 1
            
            greatest = max(greatest, node.val)

            dfs(node.left, greatest)
            dfs(node.right, greatest)

        dfs(root, float("-inf"))

        return self.good_node_count

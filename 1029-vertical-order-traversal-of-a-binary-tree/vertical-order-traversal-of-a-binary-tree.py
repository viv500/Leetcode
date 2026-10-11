from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        columns = defaultdict(list)

        def dfs(node, col, row):
            if not node: return

            columns[col].append([row, col, node.val])
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        columns = list(columns.items())
        columns.sort()
        for c in columns:
            c[1].sort()

        result = []
        for c in columns:
            column = []
            for _, _, val in c[1]:
                column.append(val)
            result.append(column)

        return result
        
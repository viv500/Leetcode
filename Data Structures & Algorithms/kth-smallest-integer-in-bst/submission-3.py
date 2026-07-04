# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        stack = []

        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()
            lst.append(node.val)
            if node.right:
                cur = node.right

        return lst[k - 1]
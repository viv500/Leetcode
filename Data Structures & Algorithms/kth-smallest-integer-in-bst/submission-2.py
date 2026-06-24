# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        inorder = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            popped = stack.pop()
            inorder.append(popped.val)

            cur = popped.right

        return inorder[k - 1]

        

        
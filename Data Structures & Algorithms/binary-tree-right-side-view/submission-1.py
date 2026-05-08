# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # "right-side view" right-most element in each level in the in-order travseral
        if not root: return []
        output = []
        q = deque([(root)])

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                node = q.popleft()
                level.append(node)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            output.append(level[-1].val)

        return output



        
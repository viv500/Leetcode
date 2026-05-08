# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # "right-side view" right-most element in each level in the level-order travseral
        if not root: return []

        output = []
        q = deque([(root)])

        while q:
            size = len(q)
            for i in range(size):

                node = q.popleft()
                # append last node on the level (right most)
                if i == size - 1: output.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)


        return output



        
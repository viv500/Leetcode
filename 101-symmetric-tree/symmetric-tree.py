from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue1 = deque([root.left])
        queue2 = deque([root.right])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False


            # APPEND IN REVERSE ORDER FOR SYMMETRY CHECK
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.right)
            queue2.append(node2.left)
            

        return not queue1 and not queue2
        

        
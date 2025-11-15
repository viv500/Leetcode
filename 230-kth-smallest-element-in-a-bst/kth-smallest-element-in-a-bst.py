# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            current = current.right

        # while stack or current ensures that we continue traversing as long as:
        # There are nodes in the stack waiting to be processed OR
        # We have a current node to dive down from
        # need to do the deep left exploration even for left nodes




        # O(n) time and space => space optimal but not time optimal

        # def inorder_traversal(node):
            # if not node:
                # return []

            # return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        
        # sorted_elements = inorder_traversal(root)
        # return sorted_elements[k - 1]

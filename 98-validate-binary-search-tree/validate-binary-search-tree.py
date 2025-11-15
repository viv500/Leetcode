# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # we need 3a helper that keeps track of the possible upper and lowee boudns at every step
        # left chlid inherits lower bound from parents, right child inherits upper bound
        # left child's upper bound is the parents value, right chiild's lower bound is parent
        def BSTHelper(node, upper, lower):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            return BSTHelper(node.left, node.val, lower) and BSTHelper(node.right, upper, node.val)

        
        return BSTHelper(root, float('inf'), float('-inf'))



        

        # this validates BST parent to children rule but not larger BST rule
        # if not root:
         #   return True # base case
        
        #if not root.left and not root.right:
           # return root.val

        #return self.isValidBST(root.left) < root.val < self.isValidBST(root.right)
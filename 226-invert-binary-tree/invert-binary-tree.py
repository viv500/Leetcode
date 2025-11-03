# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        # binary doesnt need to have 2 children

        if not root:
            return None


        #  to avoid wasted space with temp
        root.left, root.right = root.right, root.left


        # need self to call any member function
        self.invertTree(root.left)
        self.invertTree(root.right)


        # dont need a dummy root cuz we never parse root itself, we just keep sending references of its children back to the recursive call


        return root

        # O(n)
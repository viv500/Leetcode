# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        #preorder: dfs from left most chain to rightmost chain

        if not root:
            return []

        node_stack = []
        traversal = []
        node_stack.append(root)

        while(node_stack):
            node = node_stack.pop()

            traversal.append(node.val)
            if node.right: node_stack.append(node.right)
            if node.left: node_stack.append(node.left) # pushing right left child last: it will ALWAYS get popped firsst
    

        return traversal


        
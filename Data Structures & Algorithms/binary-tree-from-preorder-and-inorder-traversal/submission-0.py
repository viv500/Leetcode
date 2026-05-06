# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # in order: bst order
        # pre order: recursively go to left until empty, go back, go to the right, continue

        # pre order gives us info about root (index 0) and the recursive in order left paths
        # however, we don't know which elements are to the left and right of root

        # in order splits the left and right halfs to separate sides of the root
        # once we identify root from pre order traversal, any elements to the left of that root in
        # the in order travsersal is in the left usb tree, and right to the root is in the right subtree

        if not preorder or not inorder: return None

        root = TreeNode(val=preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
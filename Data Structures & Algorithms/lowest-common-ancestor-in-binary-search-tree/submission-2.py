# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # binary SEARCH tree!
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # if a particular node is in betwen p and q, then it MUST be the LCA 
        # since in a bst, this would mean p and q are on different sides. and any more branching means it no longer is a 
        # common ancestor

        cur = root

        while cur:
            # we dont if p is < q
            if (p.val <= cur.val <= q.val) or (p.val >= cur.val >= q.val): return cur

            # if not, both p and q are on the same side (left or right)
            # both on left
            elif p.val <= cur.val:
                cur = cur.left

            # both on right
            else:
                cur = cur.right
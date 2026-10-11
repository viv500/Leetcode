# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def dfs(r1, r2):
            if not r1 and not r2: return True
            if not r1 or not r2: return False

            return r1.val == r2.val and dfs(r1.left, r2.left) and dfs(r1.right, r2.right)


        if root.val == subRoot.val and dfs(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
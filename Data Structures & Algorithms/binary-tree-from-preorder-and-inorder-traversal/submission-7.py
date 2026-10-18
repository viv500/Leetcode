# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}
        pre = 0

        def build(lo, hi):
            if lo >= hi: return None
            nonlocal pre

            root = TreeNode(preorder[pre])
            mid = idx[root.val]
            pre += 1

            root.left = build(lo, mid)
            root.right = build(mid + 1, hi)

            return root

        return build(0, len(preorder))
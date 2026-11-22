# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {n: i for i,n in enumerate(inorder)}
        root_index = 0
        def build(lo, hi):
            nonlocal root_index
            if lo >= hi: return None

            node = TreeNode(preorder[root_index])
            root_index += 1
            
            mid = idx[node.val]
            
            node.left = build(lo, mid)
            node.right = build(mid + 1, hi)
            
            return node

        return build(0, len(preorder))
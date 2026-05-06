# preorder = tells us ROOT first
# inorder = tells us LEFT vs RIGHT split of a subtree

# key idea:
# inorder lets us find how big the left subtree is (mid index)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        # root is always first in preorder
        root = TreeNode(preorder[0])

        # find root position in inorder → splits left/right subtree
        mid = inorder.index(preorder[0])

        # everything left of mid in inorder = left subtree
        # everything right of mid = right subtree
        #
        # so left subtree size = mid

        root.left = self.buildTree(
            preorder[1:mid+1],   # next 'mid' nodes belong to left subtree
            inorder[:mid]
        )

        root.right = self.buildTree(
            preorder[mid+1:],    # remaining nodes go right
            inorder[mid+1:]
        )

        return root
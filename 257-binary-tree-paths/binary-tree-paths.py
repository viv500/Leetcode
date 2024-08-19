class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        main = []

        def backtrack(path: str, node: Optional[TreeNode]):
            if not node:
                return

            # If it's a leaf node, append the path to the result list
            if not node.left and not node.right:
                main.append(path)
                return

            # Extend the path with the current node's value and recursively explore children
            if node.left:
                backtrack(f"{path}->{node.left.val}", node.left)
            if node.right:
                backtrack(f"{path}->{node.right.val}", node.right)

        # Initialize the backtrack function with the root's value
        if root:
            backtrack(str(root.val), root)

        return main

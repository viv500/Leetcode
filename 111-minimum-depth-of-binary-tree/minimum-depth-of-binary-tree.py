# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root):
        # BFS approach
        # If the tree is empty, return 0
        if not root:
            return 0

        # Initialize the queue with the root node and its depth (1)
        queue = deque([(root, 1)])

        # Perform BFS (Breadth-First Search)
        while queue:
            # Dequeue a node along with its depth
            node, depth = queue.popleft()

            # If the node is a leaf, return its depth
            if not node.left and not node.right:
                return depth

            # Add left child to the queue if it exists
            if node.left:
                queue.append((node.left, depth + 1))

            # Add right child to the queue if it exists
            if node.right:
                queue.append((node.right, depth + 1))

        # This will never be reached since we return when we find a leaf
        return 0

        #dfs approach: (not the most efficient)
        '''def minDepth(root: TreeNode) -> int:
        # Base case: If the tree is empty, return 0
        if not root:
            return 0

        # If there is no left subtree, we return the min depth of the right subtree (if any)
        if not root.left:
            return minDepth(root.right) + 1
        
        # If there is no right subtree, we return the min depth of the left subtree (if any)
        if not root.right:
        return minDepth(root.left) + 1

    # Otherwise, return the min depth of the left and right subtree + 1 (for current root)
    return min(minDepth(root.left), minDepth(root.right)) + 1'''
        
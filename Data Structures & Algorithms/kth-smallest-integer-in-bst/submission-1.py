# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative approach: O(n) time O(h) space
        # keep adding elements all the way to the left, once no moore, take the most recent left, go right, repeat
        cur = root
        stack = []
        result = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            result.append(cur.val)

            cur = cur.right

        return result[k - 1]


        self.output = []
        self.count = 0
        self.result = None

        # recursive approach: O(n) time  O(h) space (recursive call stack, O(log n) for balanced tree, O(n) for skwewed)
        # either construct in order traveral array and return kth eleemnt, or stop early
        def dfs(root):

            if not root or self.result is not None: return

            dfs(root.left)

            self.output.append(root.val)
            self.count += 1
            if self.count == k:
                self.result = root.val
                return
                
            dfs(root.right)

        dfs(root)

        return(self.result)


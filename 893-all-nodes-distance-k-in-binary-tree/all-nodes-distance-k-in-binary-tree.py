# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        result = []

        def dfs(root):
            if not root: return

            if root.left: parents[root.left] = root
            if root.right: parents[root.right] = root

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        q = deque([target])
        visited = set()

        # run bfs k times
        for dist in range(k + 1):
            # only expand frontier
            for _ in range(len(q)):
                node = q.popleft()
                if node in visited: continue
                visited.add(node)
                
                if dist == k: result.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if node in parents: q.append(parents[node]) # i.e. not root

        return result
            



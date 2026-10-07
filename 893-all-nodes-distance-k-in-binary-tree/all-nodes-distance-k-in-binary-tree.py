# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        q = deque([root])
        result = []

        # bfs to map each node to its parent
        while q:
            node = q.popleft()
            if node.left: 
                parent[node.left] = node
                q.append(node.left)
            
            if node.right:
                parent[node.right] = node
                q.append(node.right)

        q.append(target)
        visited = set()
        print(parent)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visited: continue
                if k == 0: 
                    result.append(node.val)
                    continue

                visited.add(node)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if node in parent: q.append(parent[node])
            
            k -= 1

        return result

            


        




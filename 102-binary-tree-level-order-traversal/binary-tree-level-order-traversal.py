from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        
        if not root:
            return []

        # need a for loop that pops the number of same-level nodes from the queue

        queue = deque([root])
        output = []

        while(queue):
            level_size = len(queue) # all the nodes in the queue will be from the same level
            level_list = [] # within while loop so it resets for each level

            for _ in range(level_size):
                node = queue.popleft()
                level_list.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # we reach here after all nodes from the same level are added to queue and nothing else
            output.append(level_list)

        return output
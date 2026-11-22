"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        mapp = {}

        node = head
        
        while node:
            mapp[node] = Node(node.val)
            node = node.next

        for node in mapp:
            mapp[node].next = mapp[node.next] if node.next else None
            mapp[node].random = mapp[node.random] if node.random else None

        return mapp[head]
        
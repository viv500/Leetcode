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
        otn = {}
        root = head
        cur = head

        while cur:
            otn[cur] = Node(cur.val)
            cur = cur.next

        cur = root
        while cur:
            otn[cur].next = otn[cur.next] if cur.next else None
            otn[cur].random = otn[cur.random] if cur.random else None
            cur = cur.next
        
        return otn[root]

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
        old_to_new = {}
        cur = head

        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            old_to_new[cur].next = old_to_new[cur.next] if cur.next else None
            old_to_new[cur].random = old_to_new[cur.random] if cur.random else None
            cur = cur.next


        return old_to_new[head] if head else head


        
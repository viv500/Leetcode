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
        # deep copy problem could be done in 1 pass cuz neighbbors are guarenteed
        # to already exist
        # here, 2 passes are needed
        if not head: return None

        old_to_new = {head: Node(x = head.val)} # need to init here
        cur = head

        # 1st pass
        while cur.next:
            old_to_new[cur.next] = Node(x = cur.next.val)
            old_to_new[cur].next = old_to_new[cur.next]

            cur = cur.next

        for old, new in old_to_new.items():
            if old.random:
                new.random = old_to_new[old.random]
            else:
                new.random = None

        return old_to_new[head]

        

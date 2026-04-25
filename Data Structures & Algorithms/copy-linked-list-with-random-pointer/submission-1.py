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
        # deep copy problem could be done in 1 pass cuz neighbbors are guarenteed to already exist
        # this is a linked list, simple while loop not dfs
        # here, 2 passes are needed
        if not head: return None

        old_to_new = {} # need to init here
        cur = head

        while cur:
            # creating the nodes in the hashmap
            if cur not in old_to_new:
                old_to_new[cur] = Node(x = cur.val)
            if cur.next and cur.next not in old_to_new:
                old_to_new[cur.next] = Node(x = cur.next.val)
            if cur.random and cur.random not in old_to_new:
                old_to_new[cur.random] = Node(x = cur.random.val)

            # creating the connections (get handles the Null case)
            old_to_new[cur].next = old_to_new.get(cur.next, None)
            old_to_new[cur].random = old_to_new.get(cur.random, None)

            cur = cur.next
            
        return old_to_new[head]

        

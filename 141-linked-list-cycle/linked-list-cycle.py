# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # floyds tortoise and hare method
        

        # cycle detection using slow and fast pointer
        # comparing node1 == node 2 is correct, comparing values is not cuz it can have repeating values

        if not head or not head.next:
            return False


        node1 = head
        node2 = head.next


        while node1 and node2:
            if node1 == node2:
                return True

            if not node2.next or not node2.next.next:
                return False # dont want to call next on None, assert this first
            
            node1 = node1.next
            node2 = node2.next.next


        # we've reached a terminal node, not a cyclical graph
        return False
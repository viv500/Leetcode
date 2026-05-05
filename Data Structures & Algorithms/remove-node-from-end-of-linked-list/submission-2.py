# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 2 pointer approach - 1 moves n steps ahead and then both move together until one of them hits the end
# at that point, the other pointer will be at the nth last node

# NOTE: create a dummy prev for the head, to handle edge case where the head needs to be deletec
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        # move slow n steps forward
        for _ in range(n):
            if fast: fast = fast.next

        # move them together
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # now slow sits at the node right before the nth last
        if slow and slow.next: slow.next = slow.next.next

        return dummy.next
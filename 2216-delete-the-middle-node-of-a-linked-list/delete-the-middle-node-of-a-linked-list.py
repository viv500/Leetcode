# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #edge cases
        if not head:
            return head

        if not head.next:
            return head.next

        length = 0

        # to find the length of linkedlist
        dummy1 = head

        while dummy1:
            length += 1
            dummy1 = dummy1.next

        mid = length // 2

        # to remove the middle
        dummy2 = head

        while head and head.next:
            if mid == 1: #so that we dont actually land on the middle
                head.next = head.next.next
                head = head.next
                mid -= 1
            else:
                mid -= 1
                head = head.next

        return dummy2
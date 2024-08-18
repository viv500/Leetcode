# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # new = head.next is find for stroing the pointer but when you head.next = head.next.next, it gets rid of that
        # head.next you assigned to new. now the head.next is different

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:

            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next

        return dummy.next


        
            




        
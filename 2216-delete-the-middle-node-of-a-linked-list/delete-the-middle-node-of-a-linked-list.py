# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # better method: single pass using slow and fast pointer (double the speed)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #edge cases
        if not head:
            return head

        if not head.next:
            return head.next

        dummyslow = head
        dummyfast = head

        # won't be null reference cuz we got rid of that. we need this so that slow pointer
        # is 1 step behind middle element when the fast pointer reaches the end
        dummyfast = dummyfast.next.next

        # we're doing double skips so we gotta check the next pointer too
        while dummyfast and dummyfast.next:
            dummyslow = dummyslow.next
            dummyfast = dummyfast.next.next

        dummyslow.next = dummyslow.next.next

        return head


        ''' issue: 2 separate traversals for length and deletion

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
        '''
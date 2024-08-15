# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # edge case
        if not head:
            return head

        odd = head
        even = head.next
        start = even # to keep track of start of even linkedlist

        while even and even.next:
            odd.next = even.next #linking odd pointer to odd pointer
            odd = odd.next #moving to next pointer
            even.next = odd.next #linking even pointer to even pointer
            even = even.next # moving to next pointer

        odd.next = start

        return head


        """ failed: creating new nodes and linking can case cycles!!

        dummyodd = ListNode(0)
        currentodd = dummyodd

        dummyeven = ListNode(0)
        currenteven = dummyeven

        odd = True

        while head:
            if(odd):
                currentodd.next = head
                currentodd = currentodd.next
                head = head.next
                odd = False
            else:
                currenteven.next = head
                currenteven = currenteven.next
                head = head.next
                odd = True

        currentodd.next = dummyeven.next

        return dummyodd.next
        """
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode(head.val)
        current = dummy

        visited = [head.val]

        head = head.next

        while head:
            if head.val not in visited:
                visited.append(head.val)
                current.next = head
                current = current.next
                head = head.next
            else:
                head = head.next

        current.next = None

        return dummy


        
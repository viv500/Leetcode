# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next: return head

        middle = head
        fast = head.next

        while fast and fast.next:
            middle = middle.next
            fast = fast.next.next

        left = head
        right = middle.next
        middle.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        dummy = ListNode()
        cur = dummy

        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next

        cur.next = left or right # will pick the one thats non Null

        return dummy.next



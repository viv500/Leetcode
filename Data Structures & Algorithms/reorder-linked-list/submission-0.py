# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find middle of list using slow-fast pointers
        # 2. reverse second half of list
        # 3. interleave list1 and list2 (splice 2nd into 2st, dont create new)
        if not head: return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow finished 1 behind, if odd, middle goes in right
        cur = slow.next
        slow.next = None

        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
            
        

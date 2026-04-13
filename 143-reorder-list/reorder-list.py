# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # note: midpoint for odd length -> middle is included in left
        
        # 1. find middle of list using fast-slow pointers (need to cut in half)
        # 2. reverse second half of linked list
        # 3. alternte between elements of first half and reversed second half

        #1. 
        if not head: return

        start_1 = head

        # head starts 1 step ahead to make the mid point logic work for odd and even length
        slow, fast, = head, head.next

        while fast and fast.next: # don't need to check slow
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None

        print(cur)

        #2. 
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        start_2 = prev
        # cur now contains Null and prev contains the first element of reversed list  
        #3.

        # note: list 2 is guarenteed to be the same size or shorter as list 1
        while start_2:
            nxt_1, nxt_2 = start_1.next, start_2.next

            start_1.next = start_2
            start_2.next = nxt_1
            start_1 = nxt_1
            start_2 = nxt_2

        return head

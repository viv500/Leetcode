# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Time O(n), Space O(1)
        """
        Do not return anything, modify head in-place instead.

        Approach:
          1. Find the middle of the list using fast/slow pointers, and split
             the list into two halves. For odd-length lists, the middle node
             stays with the first half.
          2. Reverse the second half.
          3. Interleave nodes from the first half with the reversed second half.
        """
        if not head:
            return

        # 1. Split the list in half.
        # Starting `fast` one step ahead makes the split work cleanly for
        # both even and odd lengths (left half ends up >= right half).
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None  # terminate the first half

        # 2. Reverse the second half in place.
        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second = prev

        # 3. Interleave the two halves.
        # The second half is guaranteed to be the same length or shorter
        # than the first, so we iterate until `second` is exhausted.
        while second:
            nxt_1, nxt_2 = first.next, second.next
            first.next = second
            second.next = nxt_1
            first, second = nxt_1, nxt_2
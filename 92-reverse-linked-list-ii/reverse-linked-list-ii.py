# note: need to allow ends of reversed list to switch what they point to
# typically in reversal, prev is the start of the list and cur is None (1 AHEAD of first)
# here, prev is 4 and cur is 5 (node after reversed list)
# before is 1, before.next is 2. need 2 to point to cur so before.next.next = cur
# need 1 to point to 4. so before.next = prev
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0, head)
        before = dummy
        # 1. normal traversal
        for _ in range(left - 1):
            before = before.next

        # 2. reversal
        prev = None
        cur = before.next
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # 3. switch head and tail
        before.next.next = cur
        before.next = prev

        return dummy.next
        
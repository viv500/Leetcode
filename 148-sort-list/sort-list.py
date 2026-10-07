# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: return head

        mid = self.getMid(head)
        left, right = mid, mid.next
        left.next = None

        left, right = self.sortList(head), self.sortList(right)
        return self.merge(left, right)

    def getMid(self, node):
        slow = node
        fast = node.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge(self, left, right):
        res = ListNode()
        cur = res
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            
            cur = cur.next
        
        if left: cur.next = left
        if right: cur.next = right

        return res.next

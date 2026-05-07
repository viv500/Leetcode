# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""

        while l1:
            a = str(l1.val)+ a
            l1 = l1.next

        while l2:
            b = str(l2.val) + b
            l2 = l2.next

        summ = str(int(a) + int(b))[::-1]
        print(summ)

        result = ListNode()
        cur = result

        for digit in summ:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return result.next
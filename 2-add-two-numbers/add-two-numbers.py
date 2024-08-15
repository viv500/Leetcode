# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # dont convert to strings and ints, extra space complexity
        # keep track of carry over number and add numbers to node while iterating through linkedlists

        dummy = ListNode(0)
        current = dummy
        carry = 0

        # ensures carry isnt ignored even when both lists have been traversed completely
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry

            # carry for next is the tens place of the current total
            carry = total // 10
            # digit to add to new nummber is units place of total
            to_add = total % 10

            current.next = ListNode(to_add)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        nums = set(nums)

        cur = dummy
        nxt = dummy.next

        while nxt:

            # if nxt value is in lisyt, skip that node
            if nxt.val in nums:
                cur.next = nxt.next
            else:
                # proceed as usual
                cur = cur.next

            # always move nxt, only move cur when you find vals you wanna remove
            nxt = nxt.next
        
        return dummy.next
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # initialize dummy Node
        dummy = ListNode()
        # need to keep the start of this , so store it and use a different node for iterations
        head = dummy

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1
        else:
            head.next = list2
            

        # we dont want the 0 vertex from constructor
        return dummy.next
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# min heap to track smallest element at every point
# insert both value and the actual node object so we can keep track
# note: need a monotonic counter to break ties between values since we dont want 2 ListNode objects to be compared in the tuple

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = 0
        minHeap = []

        for lst in lists:
            heapq.heappush(minHeap, (lst.val, counter, lst))
            counter += 1

        print(minHeap)

        dummy = cur = ListNode()

        while minHeap:
            value, count, node = heapq.heappop(minHeap)
            if node.next: 
                counter += 1
                heapq.heappush(minHeap, (node.next.val, counter, node.next))

            node.next = None
            cur.next = node
            cur = cur.next

        return dummy.next
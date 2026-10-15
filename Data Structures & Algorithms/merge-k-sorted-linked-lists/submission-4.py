# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        minHeap = []
        nid = 0
        for l in lists:
            if l: heapq.heappush(minHeap, (l.val, nid, l))
            nid += 1

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next

            if node.next: 
                heapq.heappush(minHeap, (node.next.val, nid, node.next))
                nid += 1
    


        return dummy.next


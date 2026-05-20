# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        minHeap = []
        newList = ListNode()
        cur = newList
        counter = 0

        for lst in lists:
            if lst: 
                counter += 1
                heapq.heappush(minHeap, (lst.val, counter, lst))

        while minHeap:
            value, _, node = heapq.heappop(minHeap)
            nei = node.next

            if nei: 
                counter += 1
                heapq.heappush(minHeap, (nei.val, counter, nei))

            cur.next = node
            cur = cur.next

        return newList.next
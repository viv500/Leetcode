import heapq
class Solution:
    # need a max heap to get rid of the largest elements
    # time: n log k (log k per heap insertion/deletion)
    # space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush_max(maxHeap, (dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        return [[h[1], h[2]] for h in maxHeap]

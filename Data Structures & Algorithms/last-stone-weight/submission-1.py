import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # "pick the 2 heaviest" -> sort + heapq
        maxHeap = []
        for stone in stones: # n log n
            heapq.heappush_max(maxHeap, stone)

        while len(maxHeap) >= 2:
            a = heapq.heappop_max(maxHeap)
            b = heapq.heappop_max(maxHeap)

            heapq.heappush_max(maxHeap, abs(a - b))

        return heapq.heappop_max(maxHeap)
        
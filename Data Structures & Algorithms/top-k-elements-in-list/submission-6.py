from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time and space
        count = Counter(nums)

        # O(n) time and space
        count = list(count.items())

        # O(n log n) time

        heap = []

        for num, c in count:
            heapq.heappush(heap, (c, num))
            if len(heap) > k:
                heapq.heappop(heap)

        #O(k)
        return [h[1] for h in heap]

        # overall time: O(n log n)
        # overall space: O(n)
        
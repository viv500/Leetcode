import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n log n)
        count = Counter(nums)

        heap = []
        for num, amount in count.items():
            heapq.heappush(heap, (amount, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for value, num in heap]

        elements = list(count.items())
        elements.sort(key=lambda t: t[1])
        return [e[0] for e in elements[-1:-k-1:-1]]

        # O(n log k) great is k << n (heap size never bigger than k)
        # min heap approahc -> stack size exceeds k? remove least occuring (min)
        





import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n log n)
        count = Counter(nums)
        elements = list(count.items())
        elements.sort(key=lambda t: t[1])
        return [e[0] for e in elements[-1:-k-1:-1]]

        
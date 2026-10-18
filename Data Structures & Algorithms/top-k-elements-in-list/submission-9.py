from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        m = [(c,v) for v,c in count.items()]
        heapq.heapify_max(m)
        result = []
        while k > 0 and m:
            result.append(heapq.heappop_max(m)[1])
            k -= 1
        return result
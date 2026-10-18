from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for c in count:
            buckets[count[c]].append(c)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for val in bucket:
                if k > 0:
                    result.append(val)
                    k -= 1

        return result

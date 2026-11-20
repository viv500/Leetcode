from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []
        count = Counter(nums)

        for n,c in count.items():
            buckets[c].append(n)

        for i in range(len(nums), -1, -1):
            bucket = buckets[i]
            for n in bucket:
                if len(result) == k: return result
                result.append(n)

        return result

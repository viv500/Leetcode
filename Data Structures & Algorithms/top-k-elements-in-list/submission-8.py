from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = list(count.items())
        count.sort(key = lambda s: s[1], reverse=True)

        return [v for v,c in count][:k]
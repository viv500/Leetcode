from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        count = list(count.items())
        count.sort(key = lambda s: s[1], reverse = True)
        return [c[0] for c in count][:k]
        
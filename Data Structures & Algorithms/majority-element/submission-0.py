from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for v in count:
            c = count[v]
            if c >= math.floor(len(nums) // 2): return v
        
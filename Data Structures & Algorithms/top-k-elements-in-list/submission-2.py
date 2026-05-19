from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        nums = [[count, value] for value,count in nums.items()]
        nums.sort(reverse=True)
        return [pair[1] for pair in nums[:k]]
        
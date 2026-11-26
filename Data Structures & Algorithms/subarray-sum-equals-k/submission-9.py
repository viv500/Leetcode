from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefixes[0] = 1
        total = 0
        result = 0

        for num in nums:
            total += num
            result += prefixes[total - k]
            prefixes[total] += 1

        return result






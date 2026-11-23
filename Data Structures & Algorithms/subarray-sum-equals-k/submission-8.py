from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running = 0
        total = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        for n in nums:
            running += n
            total += prefix_sum[running - k]
            prefix_sum[running] += 1

        return total



from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        k_subarray_count = 0
        running_total = 0

        for i in range(len(nums)):
            running_total += nums[i]       

            target = running_total - k
            if target in prefix_count:
                k_subarray_count += prefix_count[target]

            prefix_count[running_total] += 1

        return k_subarray_count
        
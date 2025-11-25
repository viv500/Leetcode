class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        min_size = float('inf')
        R = L = 0

        while R < len(nums):
            summ += nums[R]

            while summ >= target:
                min_size = min(min_size, R - L + 1)
                summ -= nums[L]
                L += 1
            R += 1
        return 0 if min_size == float('inf') else min_size
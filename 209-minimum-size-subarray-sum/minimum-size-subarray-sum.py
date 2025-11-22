class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = R = summ = 0
        minimum_size = float('inf')

        while R < len(nums):
            summ += nums[R]
            R += 1

            while summ >= target:
                summ -= nums[L]
                L += 1
                minimum_size = min(R - L + 1, minimum_size)

        return 0 if minimum_size == float('inf') else minimum_size

            

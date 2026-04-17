class Solution:
    def rob(self, nums: List[int]) -> int:
        # split into 2 distinct cases and find max : where last is included and where last is excluded
        if len(nums) == 1: return nums[0]

        def max_money(nums):
            if not nums: return 0
            if len(nums) == 1: return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return dp[len(nums) - 1]

        
        return max(max_money(nums[1:]), max_money(nums[:len(nums) - 1]))
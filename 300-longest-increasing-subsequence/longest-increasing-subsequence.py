class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # intuition: dp[i] stores longest subsequence ending at ith index
        # Time: O(n^2) and O(n) space complexity

        n = len(nums)
        dp = [1] * n # initialise all indices having longest subsequence 1 (itself)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]: # if longer subsequence can be formed
                # longest subsequence is either current of the one formed at j, + 1 step to i
                    dp[i] = max(dp[i], dp[j] + 1)
        # the longest one doesnt end at dp[n - 1]
        return max(dp)
        
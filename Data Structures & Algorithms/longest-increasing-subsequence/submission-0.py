class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # !!! NOTE - LIS different from LCS
        # O(N^2) time O(N) space
        # nested for loop, i iterates through list, j iterates from 0 to i
        # this would allow us to find the longest possible and not just ANY increasing subsequence

        # dp[n] is the longest subsequence STARTING at n, this would mean sol is max(dp), which is not typical
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



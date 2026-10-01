class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index):
            if index >= len(nums): return 0

            if index in dp: return dp[index]

            dp[index] = max(dfs(index + 1), nums[index] + dfs(index + 2))
            return dp[index]


        return dfs(0)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index):
            if index in dp: return dp[index]
            if index >= len(nums): return 0

            # take
            take = nums[index] + dfs(index + 2)
            #leave
            leave = dfs(index + 1)

            dp[index] = max(take, leave)
            return dp[index]


        return dfs(0)
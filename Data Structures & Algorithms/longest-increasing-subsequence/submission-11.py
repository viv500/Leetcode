class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index, prev):
            if index == len(nums): return 0

            if (index, prev) in dp: return dp[(index, prev)]

            LIS = dfs(index + 1, prev)
            if prev < nums[index]:
                LIS = max(1 + dfs(index + 1, nums[index]), LIS)

            dp[(index, prev)] = LIS
            return dp[(index, prev)]

        return dfs(0, float("-inf"))
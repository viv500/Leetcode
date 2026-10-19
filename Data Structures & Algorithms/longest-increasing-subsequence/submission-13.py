class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index, prev):
            if index == len(nums): return 0

            if (index, prev) in dp: return dp[(index, prev)]

            if prev < nums[index]:
                dp[(index, prev)] = 1 + dfs(index + 1, nums[index])
            
            dp[(index, prev)] = max(dp.get((index, prev), 0), dfs(index + 1, prev))

            return dp[(index, prev)]

        return dfs(0, float("-inf"))

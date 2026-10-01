class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(index, total):
            if index >= len(nums): return total

            if (index, total) in dp: return dp[(index, total)]

            dp[(index, total)] = max(dfs(index + 1, total), dfs(index + 2, total + nums[index]))
            return dp[(index, total)]


        return dfs(0, 0)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0 : return False
        target = summ // 2
        dp = {}
        def dfs(index, curSum):
            if index == len(nums): return curSum == target
            if (index, curSum) in dp: return dp[(index, curSum)]

            dp[(index, curSum)] = dfs(index + 1, curSum) or dfs(index + 1, curSum + nums[index])
            return dp[(index, curSum)]

        return dfs(0, 0)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0: return False
        half_target = target // 2
        dp = {}
        def dfs(index, curSum):
            if (index, curSum) in dp: return dp[(index, curSum)]

            if curSum == half_target: return True
            if index == len(nums): return False

            # either take or don't take
            dp[(index, curSum)] = dfs(index + 1, curSum) or dfs(index + 1, curSum + nums[index])

            return dp[(index, curSum)]
        
        return dfs(0, 0)
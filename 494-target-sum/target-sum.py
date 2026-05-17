class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        def dfs(index, curSum):
            if (index, curSum) in dp:
                return dp[(index, curSum)]

            if index == len(nums):
                return 1 if curSum == target else 0
            
            dp[(index, curSum)] = dfs(index + 1, curSum - nums[index]) + dfs(index + 1, curSum + nums[index])

            return dp[(index, curSum)]

        
        return dfs(0, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # top down DP O(m * n) , same brute force but with caching
        dp = {} # (index, cuSum) -> ways

        def dfs(index, curSum):
            if (index, curSum) in dp: return dp[(index, curSum)]
            if index == len(nums):
                return 1 if curSum == target else 0

            dp[(index, curSum)] = (
                dfs(index + 1, curSum + nums[index]) + dfs(index + 1, curSum - nums[index])
            )

            return dp[(index, curSum)]

        
        # dfs(0, 0) is all ways of reaching target starting at index i and starting at sum 0
        # also this is top down
        return dfs(0, 0)

    
        # brute force: + or - decision, O(2^n)

        def dfs(index, curSum):

            if index == len(nums):
                return 1 if curSum == target else 0

            return dfs(index + 1, curSum + nums[index]) + dfs(index + 1, curSum - nums[index])

        
        return dfs(0, 0)

        
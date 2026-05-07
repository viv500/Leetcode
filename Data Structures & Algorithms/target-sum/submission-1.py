class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute force: + or - decision, O(2^n)

        def dfs(index, curSum):

            if index == len(nums):
                return 1 if curSum == target else 0

            return dfs(index + 1, curSum + nums[index]) + dfs(index + 1, curSum - nums[index])

        
        return dfs(0, 0)

        
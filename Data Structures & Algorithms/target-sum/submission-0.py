class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute force: + or - decision, O(2^n)
        ways = 0
        def dfs(index, curSum):
            nonlocal ways

            if index == len(nums):
                if curSum == target: 
                    ways += 1
                return

            dfs(index + 1, curSum + nums[index])
            dfs(index + 1, curSum - nums[index])

        
        dfs(0, 0)
        return ways


   
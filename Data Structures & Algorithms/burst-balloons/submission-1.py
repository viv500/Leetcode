from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # naive solution: iterate through list and create decision tree of "pop now or dont"
        # however if you assume we "pop first", then the left and right subarrays can't really be
        # well defined subproblems since they both depend on EACHOTHER since the middle baloon was popped
        # if they depend on eachother its not really a "subproblem"

        # instead, iterate through each and "pop last". if it was popped last, then both sub arrays cannot
        # have previoulsy merged, and are indepedenent

        # to create the 1 boundary

        nums = [1] + nums + [1]
        
        @cache
        def dfs(left, right):
            if left > right:
                return 0
            best = 0
            for i in range(left, right + 1):
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                best = max(best, coins)
            return best
        
        return dfs(1, len(nums) - 2) # don't wanna include the 1 borders
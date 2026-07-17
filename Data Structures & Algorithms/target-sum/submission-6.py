class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways = 0
        def dfs(index, curSum):
            if index == len(nums):
                if curSum == target:
                    self.ways += 1
                return

            dfs(index + 1, curSum + nums[index])
            dfs(index + 1, curSum - nums[index])

        dfs(0, 0)
        return self.ways
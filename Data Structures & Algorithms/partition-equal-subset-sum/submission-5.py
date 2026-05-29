class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0: return False
        target = summ // 2

        dp = {}
        def dfs(index, cursum):
            if (index, cursum) in dp: return dp[(index, cursum)]
            if cursum == target:
                return True
            
            if index == len(nums) or cursum > target:
                return False

            dp[(index, cursum)] = dfs(index + 1, cursum) or dfs(index + 1, cursum + nums[index])
            return dp[(index, cursum)]

        return dfs(0, 0)

            
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # base case -> odd sum means impossible
        summ = sum(nums)
        if summ % 2 != 0: return False

        # target sum
        target = summ / 2
        dp = {}
        def dfs(index, cur_sum):
            if (index, cur_sum) in dp: return dp[(index, cur_sum)]
            if cur_sum == target: return True
            if index == len(nums): return False

            # either take or dont take a number
            dp[(index, cur_sum)] = dfs(index + 1, cur_sum) or dfs(index + 1, cur_sum + nums[index])

            return dp[(index, cur_sum)]

        return dfs(0, 0)
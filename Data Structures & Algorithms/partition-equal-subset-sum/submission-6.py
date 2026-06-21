class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0: return False
        target = summ // 2

        def dfs(index, curSum):
            if curSum == target: return True
            if index >= len(nums) or curSum >= target: return False
 
            # take branch and dont take branches
            return dfs(index + 1, curSum + nums[index]) or dfs(index + 1, curSum)


            

        return dfs(0, 0)
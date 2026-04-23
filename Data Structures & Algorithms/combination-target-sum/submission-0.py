class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # "all combinations" no dp has to be regular backtracking with dfs
        output = []
        combination = []

        def dfs(i, summ):
            if summ > target or i == len(nums): return

            if summ == target:
                output.append(combination.copy()) # copy so it doesnt get modified later
                return

            combination.append(nums[i])
            dfs(i, summ + nums[i]) # if we choose to include, dont (i + 1) cuz that element could be used again

            combination.pop()
            dfs(i + 1, summ) # if we choose not to include, we never want to include again

        dfs(0, 0)

        return output

            
    


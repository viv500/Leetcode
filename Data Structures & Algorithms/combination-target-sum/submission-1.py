class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def dfs(index, combination, curSum):
            if index == len(nums) or curSum > target:
                return
            if curSum == target:
                combinations.append(combination.copy())
                return
            
            value = nums[index]

            # repeat
            dfs(index, combination + [value], curSum + value)
            # skip
            dfs(index + 1, combination, curSum)

        dfs(0, [], 0)
        return combinations


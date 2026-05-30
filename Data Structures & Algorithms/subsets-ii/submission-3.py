class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        output = []

        def backtrack(i):
            if i == len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)

        return output

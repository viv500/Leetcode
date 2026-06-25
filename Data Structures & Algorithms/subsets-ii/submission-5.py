class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                output.append(subset.copy())
                return
            
            # include
            subset.append(nums[index])
            backtrack(index + 1)
            
            # exclude
            subset.pop()
            j = index
            while j < len(nums) and nums[index] == nums[j]: j += 1
            backtrack(j)

        
        backtrack(0)
        return output
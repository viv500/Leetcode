class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # can't just remove dupes cuz theyre needed in the subsets

        nums.sort()

        output = []
        subset = []

        def backtrack(index):
            if index >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)

            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1

            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        
        return output
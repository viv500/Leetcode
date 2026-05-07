class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # problem: when there are dupes, there could be a path where it is first ignored, and then taken
        # and another path where it is first taken and then ignored -> duplicate subsets

        # solution: in the "don't take" path, simply skip over all dupes of the element we skipped

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
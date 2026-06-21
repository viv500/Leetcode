class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                output.append(subset.copy())
                return

            # take
            subset.append(nums[i])
            backtrack(i + 1)

            # skip
            j = i
            while j < len(nums) and nums[j] == nums[i]: j += 1
            subset.pop()
            backtrack(j)

        backtrack(0)
        return output

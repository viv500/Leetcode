class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                subsets.append(subset[:])
                return

            # keep
            subset.append(nums[i])
            backtrack(i + 1)

            # remove
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1)

        backtrack(0)
        return subsets

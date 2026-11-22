class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(subset[:])
                return

            n = nums[index]

            subset.append(n)
            backtrack(index + 1)

            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result
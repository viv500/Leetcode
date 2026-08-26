class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                solution.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return solution
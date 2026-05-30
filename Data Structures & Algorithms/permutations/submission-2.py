class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        permutation = []
        output = []
        def backtrack():
            if len(permutation) == len(nums):
                output.append(permutation.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    visited.add(nums[i])
                    permutation.append(nums[i])

                    backtrack()

                    visited.remove(nums[i])
                    permutation.pop()

        backtrack()

        return output

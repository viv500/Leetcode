class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        used = [False] * len(nums)
        permutation = []
        def backtrack():
            if len(permutation) == len(nums):
                output.append(permutation.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    backtrack()
                    used[i] = False
                    permutation.pop()

        backtrack()

        return output
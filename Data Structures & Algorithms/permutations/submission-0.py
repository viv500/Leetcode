class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)
        output = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                output.append(permutation.copy()) # without copy, all permutatinos would be empty
                return

            # loop so don't need to call backtrasck() again
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    permutation.append(nums[i])
                    backtrack()
                    visited[i] = False
                    permutation.pop()


        backtrack()
        return output


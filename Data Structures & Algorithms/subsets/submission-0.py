class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs naturally makes every "take" or "skip" decision
        output = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)

        return output

            

        



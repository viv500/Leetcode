class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # need 2 separate recursive calls cuz theres no loop making the choice
        output = []
        subset = []

        def backtrack(index):
            if index == len(nums): 
                output.append(subset.copy())
                return

            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            backtrack(index + 1)

        backtrack(0)

        return output
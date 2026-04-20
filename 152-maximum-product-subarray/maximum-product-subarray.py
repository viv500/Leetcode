class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # variation of kadane's algorithm, but need to worry about negative products

        # can't simply discard negatives like regular kadanes since a negative could help in the future 

        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod

            min_prod = min(num, min_prod * num)
            max_prod = max(num, max_prod * num)

            result = max(result, max_prod)

        return result
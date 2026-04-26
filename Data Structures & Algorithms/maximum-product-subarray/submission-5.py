class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # negative number always hurts
        # but 2 negatives is good
        # swapping after seeing a negative means we currently identify
        # (-) * (-) = (+) and (+) * (-) = (-)
        minProduct = nums[0]
        maxProduct = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                minProduct, maxProduct = maxProduct, minProduct

            maxProduct = max(num, maxProduct * num)
            minProduct = min(num, minProduct * num)

            result = max(result, maxProduct)

        return result

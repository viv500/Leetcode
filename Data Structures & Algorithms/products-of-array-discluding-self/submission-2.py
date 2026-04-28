class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) - prefix sum 
        # left[i] = product of all elements to the left of i excluding i
        left = [1] * len(nums)
        right = [1] * len(nums)
        left_product = 1
        right_product = 1

        for i in range(1, len(nums)):
            left_product *= nums[i - 1]
            left[i] = left_product

        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            right[i] = right_product

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]

        
        return nums




        # brute force - O(n^2)
        output = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]

            output.append(product)

        return output
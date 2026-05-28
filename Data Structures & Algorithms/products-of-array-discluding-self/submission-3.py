class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = [1] * len(nums)
        suffix_right = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_left[i] = prefix_left[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_right[i] = suffix_right[i + 1] * nums[i + 1]

        return [a * b for a,b in zip(prefix_left, suffix_right)]
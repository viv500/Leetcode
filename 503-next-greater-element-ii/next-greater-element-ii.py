class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # indices waiting for their next greater element

        for i in range(2 * n):
            num = nums[i % n]
            while stack and num > nums[stack[-1]]:
                result[stack.pop()] = num
            if i < n:
                stack.append(i)

        return result
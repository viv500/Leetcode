class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        long_nums = nums + nums
        result = [float("-inf")] * len(nums)
        stack = []

        for i,num in enumerate(long_nums):
            i = i % len(nums)
            while stack and num > stack[-1][1]:
                index, _ = stack.pop()
                result[index] = max(result[index], num)

            stack.append((i, num))

        
        return [-1 if n == float("-inf") else n for n in result]
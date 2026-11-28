# O(nlon) time and O(n) space (log n recursion depth but n slicing)
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]: 
        if len(nums) == 1: return nums
        half = len(nums) // 2

        left = self.sortArray(nums[:half])
        right = self.sortArray(nums[half:])

        result = []
        li = ri = 0

        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1

        result.extend(left[li:])
        result.extend(right[ri:])

        return result
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        result = []
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result.extend(left[l:])
        result.extend(right[r:])

        return result
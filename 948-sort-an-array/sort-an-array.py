class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(a, b):
            result = []
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
            
            result.extend(a[i:])
            result.extend(b[j:])

            return result

        if len(nums) == 1: return nums
        half = len(nums) // 2
        left, right = self.sortArray(nums[:half]), self.sortArray(nums[half:])

        return merge(left, right)
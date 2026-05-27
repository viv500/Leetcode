class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                return nums[low]
            elif nums[low] > nums[mid]:
                high = mid
            else:
                low = mid + 1

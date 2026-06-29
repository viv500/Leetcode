class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # the index to be inserted can be found by binary search if it doesnt find the actual value

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target: return mid
            elif nums[mid] > target: high = mid - 1
            else: low = mid + 1

        return low
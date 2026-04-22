class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            value = nums[mid]

            if value == target:
                return mid
            elif value > target:
                high = mid - 1
            else:
                low = mid +1
                

        return -1

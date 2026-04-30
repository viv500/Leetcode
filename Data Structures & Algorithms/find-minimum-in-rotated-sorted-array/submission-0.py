class Solution:
    def findMin(self, nums: List[int]) -> int:

        # finding minimum using binary search
        # any rotated array has 1 flipping point
        # [0 2 4 5 6]
        # [6 0 2 4 5]
        # [5 6 0 2 4]
        # [4 5 6 0 2]
        # [2 4 5 6 0]
        # as soon as regular binary order is found i.e. nums[low] <= nums[high],
        # we are guarenteed that the min is at nums[low]

        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]: # guarenteed
                return nums[low]   

            # if not, then nums[high] < nums[low]
            elif nums[low] > nums[mid]:
                # flipping point is between low and mid
                high = mid

            else: 
                # nums[high] <= nums[mid]
                # flipping point is between mid and high
                low = mid + 1
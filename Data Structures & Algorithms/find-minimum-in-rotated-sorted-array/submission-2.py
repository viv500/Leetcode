class Solution:
    def findMin(self, nums: List[int]) -> int:

        # theres exactly 1 "flipping point" where the array becomes decreasing, and then continues to be increasing

        # if nums[low] <= nums[high], we are guarenteed that the min is nums[low]
        # if nums[high] <= nums[mid], "flipping point" is on the right, so the minimum is also on the right
        # if nums[low] >= nums[mid], "flipping point" is on the rleft, so the minimum is also on the left
        # need either low or high to have mid - 1 or mid + 1, or could be infinite loop 
        #  -> make it low = mid + 1 cuz 

        # [0 1 2 3 4]
        # [4 0 1 2 3]
        # [3 4 0 1 2]
        # [2 3 4 0 1]
        # [1 2 3 4 0]

        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]: # guarenteed
                return nums[low]   

            # if not, then nums[high] < nums[low]
            elif nums[low] > nums[mid]: # has to be >, not >=
                # flipping point is between low and mid
                high = mid

            else: 
                # nums[high] <= nums[mid]
                # flipping point is between mid and high
                # need to +1 to avoid infinite loop
                low = mid + 1
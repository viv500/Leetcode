class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 3 pointer dutch national flag algoirthm
        # 0 to low: 0s
        # low to mid: 1s
        # mid to high: unexplored
        # high to end: 2s

        # dont increment mid for the 2 case cuz theres a chance we brought a 0 from the top into the middle that we need to handle
        # we increment mid in the 0 case cuz we have to deal with it later anyway, doesnt matter if its 1 or 2

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high: # theres something unexplored
            # if its 1, we can skip cuz its in the right spot
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1 # low already confirmed 0, now check the one after
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1 # high already confirmed 2, now check the one before

        
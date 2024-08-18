class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        # edge case
        if not nums or len(nums) < 3:
            return 0

        nums.sort()

        # edge case for all negatives
        if nums[-1] < 0 and nums[-2] < 0 and nums[-3] < 0:
            return nums[-1] * nums[-2] * nums[-3]


        # trivial case
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        
        # to check if first 2 valus are negative but multiply to form a larger product
        if (nums[0] * nums[1]) > (nums[-2] * nums[-3]):
            return nums[0] * nums[1] * nums[-1]
        else:
            return nums[-1] * nums[-2] * nums[-3]
        
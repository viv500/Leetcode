class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]


        nums[1] = max(nums[0], nums[1])

        # most money that can be stolen at index i is max(money at index i + max mony from 2 indices ago, max money from 1 index ago and exclude current index)

        for index in range(2, len(nums)):
            nums[index] = max(
                nums[index] + nums[index - 2],
                nums[index - 1])

        # Time Complexity: O(n)
        # Space Complexity: O(1) (in-place DP)
        # DP Type: Bottom-up dynamic programming with in-place tabulation

        return nums[len(nums) - 1]
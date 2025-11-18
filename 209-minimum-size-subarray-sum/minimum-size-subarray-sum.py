class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        L = R = 0
        smallest = float('inf')

        total = 0


        while R < len(nums):
            total += nums[R]
            R += 1

            while total >= target:
                total -= nums[L]
                L += 1
                smallest = min(smallest, R - L + 1)

        return 0 if smallest == float('inf') else smallest

        
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # sliding windows needs monotonic property: i.e. a larger window either helps or doesn't hurt, here, a negative value could hurt in the short run but help in the long run
        # need dp! Kadane's alg, kinda like greedy/sliding window

        maxSum = float('-inf')
        curSum = 0

        for num in nums:
            curSum += num

            maxSum = max(maxSum, curSum)

            if curSum < 0:
                curSum = 0


        return maxSum

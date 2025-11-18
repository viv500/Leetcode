class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        L = R = 0
        summed = 0
        minimum_length = float('inf')

        while(R < len(nums)):
            summed += nums[R]
            R += 1 # increment after so we don't skip any elements

            while(summed >= target):
                summed -= nums[L] 
                L += 1
                minimum_length = min(minimum_length, R - L + 1)

        return 0 if minimum_length == float('inf') else minimum_length
            
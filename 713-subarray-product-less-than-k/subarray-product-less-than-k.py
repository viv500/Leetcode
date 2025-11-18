class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0 or k == 1: return 0 
        # edge cases needed cuz while(product >= k): will always be true otherwise
        # also nothing can be < 1 or 0 if all aray entries are >= 1
        
        L = R = 0
        count = 0
        product = 1

        while R < len(nums):
            product *= nums[R]

            while(product >= k):
                product /= nums[L]
                L += 1

            count += R - L + 1 # KEY: if an array has product <=k , all subarrays will too
            R += 1 
        return count

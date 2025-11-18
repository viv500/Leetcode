from collections import defaultdict
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        d = defaultdict(int)
        for number in nums:
            d[number] += 1
        i = 0
        while i < len(nums):
            for zero in range(d[0]):
                nums[i] = 0
                i += 1
            for one in range(d[1]):
                nums[i] = 1
                i += 1
            for two in range(d[2]):
                nums[i] = 2
                i += 1

        return nums


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        p1 = 0
        p2 = 1

        if len(nums) == 1:
            return nums

        while p2 < len(nums):
            if nums[p1] == 0:
                if nums[p2] != 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
            else:
                p1 += 1
                p2 += 1


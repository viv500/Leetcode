class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        # 2 poiter approach

        if len(nums) == 1:
            return 1

        high = 1
        low = 0

        unique_count = 1

        while high < len(nums):
            if nums[high] == nums[low]:
                high += 1
            else:
                low += 1
                nums[low] = nums[high]
                high += 1
                unique_count += 1

        return unique_count

            
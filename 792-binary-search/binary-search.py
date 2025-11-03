class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lower = 0
        upper = len(nums) - 1

        # edge and base case: list has 1 element
        if (len(nums) == 1):
            return 0 if nums[0] == target else -1

        while lower <= upper:
            middle = (lower + upper) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                upper = middle - 1
            else:
                lower = middle + 1
        

        return -1
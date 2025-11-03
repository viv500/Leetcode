class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = dict()

        for index, item in enumerate(nums):
            compliment = target - item
            if compliment in check:
                return [index, check[compliment]]
            else:
                check[item] = index
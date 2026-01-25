class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        complements = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement in complements:
                return [complements[complement], index]
            else:
                complements[number] = index
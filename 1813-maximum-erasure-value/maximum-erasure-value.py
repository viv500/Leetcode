class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = R = 0
        highest = 0

        summ = 0
        numbers = set()

        while R < len(nums):
            summ += nums[R]
            while nums[R] in numbers:
                numbers.remove(nums[L])
                summ -= nums[L]
                L += 1

            numbers.add(nums[R])
            highest = max(highest, summ)
            R += 1

        return highest

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # XOR formula
        # since numbers start at 0 and array is 0 indexed, all matching index and number pairs wil 0 out
        # since XOR is associative and commutative, order doesn't matter
        # this wil leave the remaining number

        res = len(nums) # since the number len(nums) is in the array but theres no len(nums) index

        for i, num in enumerate(nums):
            res ^= (i ^ num)

        return res
        # O(n) time O(n) space
        '''nums = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums: return i'''

        # O(nlogn) time and O(1) space
        '''nums.sort()
        if nums[0] != 0: return 0
        if nums[len(nums) - 1] != len(nums): return len(nums)

        for i in range(1, len(nums)):
            if nums[i] != (nums[i - 1] + 1): return nums[i - 1] + 1'''
        
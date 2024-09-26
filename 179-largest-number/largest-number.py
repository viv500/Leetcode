from functools import cmp_to_key

class Solution:
    def custom_compare(self, a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    def largestNumber(self, nums: List[int]) -> str:

        # use a custom compare function for the sort function
        # 2 integers, convert to strings and append both ways and see what is larger

        # need to convert all ints to strings
        for i, n in enumerate(nums):
            nums[i] = str(nums[i])

        nums.sort(key=cmp_to_key(self.custom_compare))

        #edge case of all 0s
        return ''.join(nums) if nums[0] != "0" else "0"


    
        
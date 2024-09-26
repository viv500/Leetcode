class Solution(object):
    def twoSum(self, nums, target):
        storage = {}
        for i in range(len(nums)):
            current = nums[i]
            storage[current] = i
            check = target - current
            if check in list(storage) and nums.index(check) != i:
                return [nums.index(check), i]


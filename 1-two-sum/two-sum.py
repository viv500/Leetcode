class Solution(object):
    def twoSum(self, nums, target):
        # 2 pointer would be n log n, not great
        col = set()
        for i, j in enumerate(nums):
            if (target - j) in col:
                return [nums.index(target - j), i]

            col.add(j)


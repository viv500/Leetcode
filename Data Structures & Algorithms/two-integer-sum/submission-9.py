class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in c:
                return [c[comp], i]
            c[num] = i
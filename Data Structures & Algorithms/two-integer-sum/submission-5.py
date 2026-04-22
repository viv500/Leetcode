class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], index]
            complements[num] = index
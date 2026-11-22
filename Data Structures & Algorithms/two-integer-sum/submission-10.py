class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i,n in enumerate(nums):
            if target - n in comp:
                return [comp[target - n], i]
            
            comp[n] = i
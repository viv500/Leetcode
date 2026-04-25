class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums) == len(set(nums)) else True
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using set, O(n) time and O(n) space
        seen = set()
        for num in nums:
            if num in seen: return num
            seen.add(num)
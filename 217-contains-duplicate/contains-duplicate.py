class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for num in nums:
            if num in dups:
                return True
            else:
                dups.add(num)

        return False
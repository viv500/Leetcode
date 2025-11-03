class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sets are more optimal than lists since they are not sequential, so they have O(1) insertion, deletion, lookup etc. unlike lists that have O(n)

        # cant compare list to list(set(nums)) cuz of elements may change. also more time. comparing lengths is the easiest
        return len(nums) != len((set(nums)))
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # !!! NOTE - LCS DIFFERENT FROM LIS
        if not nums: return 0
        
        nums = set(nums)
        longest = 1

        for num in nums:
            if num - 1 not in nums:
                cur = num

                while cur + 1 in nums:
                    cur += 1
                longest = max(longest, cur - num + 1)

        return longest
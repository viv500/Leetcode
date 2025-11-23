class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = R = 0
        longest = 0
        zero_count = 0

        while R < len(nums):
            if nums[R] == 0:
                zero_count += 1
            
            while (zero_count > k):
                if nums[L] == 0:
                    zero_count -= 1
                L += 1
            
            longest = max(longest, R - L + 1)

            R += 1

        return longest
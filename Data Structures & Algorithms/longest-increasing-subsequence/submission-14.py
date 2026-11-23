class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest[i] = max(longest[i], 1 + longest[j])


        return max(longest)
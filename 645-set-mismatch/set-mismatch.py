class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        lost = -1
        dup = -1

        for i in range(1, n + 1):
            if i not in nums:
                lost = i
            if i != len(nums) and nums[i] == nums[i - 1]:
                dup = nums[i]

        return [dup, lost]

        

        
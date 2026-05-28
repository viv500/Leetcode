class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)

        return max_sum

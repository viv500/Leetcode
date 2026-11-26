class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        cur_sum = 0
        longest = 0

        while right < len(nums):
            cur_sum += nums[right]

            # shrink window as long as theres more zeros that flips available
            # zeros = (right - left + 1) - cur_sum
            while ((right - left + 1) - cur_sum) > k:
                cur_sum -= nums[left]
                left += 1

            # current window is feasible
            longest = max(longest, right - left + 1)

            right += 1

        return longest


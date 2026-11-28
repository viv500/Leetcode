class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = right = 0
        shortest = float("inf")
        total = 0

        while right < len(nums):
            total += nums[right]

            while total >= target:
                shortest = min(shortest, right - left + 1)
                total -= nums[left]
                left += 1

            right += 1

        return shortest if shortest != float("inf") else 0
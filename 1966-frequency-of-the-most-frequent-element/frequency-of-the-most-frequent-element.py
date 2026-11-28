# time: O(nlogn)
# insight: "most frequent" element must be a value thats in the original array. why?
# since we can only do add operations, getting to a higher value to be most frequent means we pass by a
# a lowe value that took strictly less steps to get to.
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = right = 0
        total = 0
        largest_frequency = 0

        # nums[right] is the value were seeing if we can get to

        while right < len(nums):
            total += nums[right]
            # shrink 
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            # this is a valid window!
            largest_frequency = max(largest_frequency, right - left + 1)
            right += 1

        return largest_frequency

        
from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_count = defaultdict(int)
        odd_count[0] = 1
        running_count = 0
        nice_subarray_count = 0

        for index, num in enumerate(nums):
            running_count += 1 if num % 2 != 0 else 0
            nice_subarray_count += odd_count[running_count - k]
            odd_count[running_count] += 1

        return nice_subarray_count

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest = 0
        running_sum_index = {}
        running_sum = 0

        for index, num in enumerate(nums):
            if num == 0: running_sum -= 1
            else: running_sum += 1

            if running_sum == 0: longest = max(longest, index + 1)
            if running_sum in running_sum_index: longest = max(longest, index - running_sum_index[running_sum])
            else: running_sum_index[running_sum] = index


        return longest

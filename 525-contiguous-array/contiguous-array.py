from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = defaultdict(int)
        prefix[0] = -1 # for the cur_sum == 0 special case that include the entire array
        cur_sum = 0
        longest = 0

        for index, num in enumerate(nums):
            cur_sum += 1 if num == 1 else -1

            if cur_sum in prefix:
                prev_index = prefix[cur_sum]
                longest = max(longest, index - prev_index)

            prefix[cur_sum] = prefix.get(cur_sum, index)

        return longest

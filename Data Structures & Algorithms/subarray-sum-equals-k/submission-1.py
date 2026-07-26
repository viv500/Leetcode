from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # is we're at index i, we want to find a j such that 
        # prefix[i] - prefix[j] = k
        # we need ro find if prefix[j] = prefix[i] - k has been seen before
        # sicne we're scanning left to right, no future indices are used

        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        count = 0

        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        

        for pre in prefix:
            target = pre - k
            if target in prefix_count:
                count += prefix_count[target]

            prefix_count[pre] += 1
        
        return count
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        count = 0
        running = 0

        for num in nums:
            running += num

            if running - k in sums:
                count += sums[running - k]
            
            sums[running] += 1

        return count


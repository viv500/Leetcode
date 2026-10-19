from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = defaultdict(int)
        p[0] = 1   
        running = 0
        total = 0
        for num in nums:
            running += num
            total += p.get(running - k, 0)
            p[running] += 1

        return total
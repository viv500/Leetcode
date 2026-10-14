from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        cur_sum = 0
        total_count = 0

        for num in nums:
            cur_sum += num
            remain = cur_sum % k

            total_count += count[remain]
            count[remain] += 1
        
        return total_count


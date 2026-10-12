from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time and space
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            buckets[c].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]
            for num in bucket:
                result.append(num)
                if len(result) == k: return result

            

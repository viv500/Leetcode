import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # O(n) bucket sort with O(n) space
        buckets = [[] for _ in range(len(nums) + 1)] # extra for 0-bucket and n-bucket

        for value, amount in count.items():
            buckets[amount].append(value) # add the value to the bucket for its specific amount

        output = []
        for i in range(len(nums), -1, -1):
            output.extend(buckets[i])

            if len(output) > k:
                return output[:k]

        




        # O(n log k) good when is k << n (heap size never bigger than k)
        # space: O(n)
        # min heap approahc -> stack size exceeds k? remove least occuring (min)

        heap = []
        for num, amount in count.items():
            heapq.heappush(heap, (amount, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for value, num in heap]

    
        # O(n log n)
        # space: O(n)
        elements = list(count.items())
        elements.sort(key=lambda t: t[1])
        return [e[0] for e in elements[-1:-k-1:-1]]




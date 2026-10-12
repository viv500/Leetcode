from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time and space
        count = Counter(nums)

        # O(n) time and space
        count = list(count.items())

        # O(n log n) time

        count.sort(key = lambda s: s[1], reverse = True)

        #O(k)
        return [c[0] for c in count[:k]]

        # overall time: O(n log n)
        # overall space: O(n)
        
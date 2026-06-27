import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        # optimal to schedule the most frequently occuring character first
        # keep track of most recently used character that we cant reuse again

        result = ""
        waiting = []
        count = Counter(s)
        maxHeap = [(count, char) for char, count in list(count.items())]
        heapq.heapify_max(maxHeap)

        while maxHeap:
            count, char = heapq.heappop_max(maxHeap)
            count -= 1
            result += char

            if waiting: heapq.heappush_max(maxHeap, waiting.pop())
            if count: waiting.append((count, char))


        return result if len(result) == len(s) else "" # handle impossible case
        
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # "pick the 2 heaviest" -> sort + heapq
        heapq.heapify_max(stones) # O(n)

        while len(stones) >= 2:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)

            heapq.heappush_max(stones, abs(a - b))

        return heapq.heappop_max(stones)
        
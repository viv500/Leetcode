import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)

            diff = abs(stone1 - stone2)

            if diff:
                heapq.heappush_max(stones, diff)

        
        return stones[0] if stones else 0


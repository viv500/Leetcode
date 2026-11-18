class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def feasible(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            return hours <= h

        while low <= high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return high + 1

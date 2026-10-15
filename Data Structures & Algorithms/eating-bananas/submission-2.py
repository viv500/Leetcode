class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        def is_feasible(k):
            time = 0
            for p in piles:
                time += math.ceil(p / k)

            return time <= h


        while low <= high:
            mid = (low + high) // 2
            if is_feasible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
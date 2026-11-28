class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        def is_feasible(capacity):
            total = 0
            d = 1
            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    d += 1

            return d <= days
        
        best = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_feasible(mid):
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return best
            

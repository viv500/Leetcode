class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        def feasible(weight):
            d = 0
            running = 0
            for w in weights:
                running += w
                if running > weight:
                    running = w
                    d += 1
            
            return d + 1 <= days

        while low <= high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low



class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search on minimum possible weight capacity
        
        low, high = max(weights), sum(weights)
        min_capacity = high

        def canShip(cap):
            d, summ = 1, 0
            for weight in weights:
                summ += weight
                if summ > cap:
                    d += 1
                    summ = weight

            return d <= days

        while low <= high:
            mid = (low + high) // 2

            if canShip(mid):
                min_capacity = mid
                high = mid - 1
            else:
                low = mid + 1

        return min_capacity

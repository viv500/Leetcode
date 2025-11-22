class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # need to decide a minimal capacity such that all weights can be shipped in days days (or ships)
        L, R, min_capacity = max(weights), sum(weights), sum(weights)

        def canShip(capacity):
            num_days, cur_capacity = 1, capacity

            for weight in weights:
                if cur_capacity - weight < 0:
                    num_days += 1
                    cur_capacity = capacity
                cur_capacity -= weight

            return num_days <= days

        while L <= R:
            capacity = (L + R) // 2
            if canShip(capacity):
                min_capacity = min(min_capacity, capacity)
                R = capacity - 1
            else:
                L = capacity + 1

        return min_capacity
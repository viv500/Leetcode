class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search on hourly rate, with ceiling being max(piles)
        # this is the max cuz any higher rate would still take 1 hour per pile
        low = 1
        high = max(piles)

        def isFeasible(rate):
            hours = 0
            for pile in piles:
                hours += ((pile + rate - 1) // rate) # integer way of doing ceil(pile // rate)

            return hours <= h

        
        while low <= high:
            mid = (low + high) // 2

            if isFeasible(mid):
                high = mid - 1
            else:
                low = mid + 1

        # this make sense since if mid was the final feasible rate, the else condition assigns low = mid + 1
        return low
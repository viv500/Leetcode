class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1000
        for p, t, f in trips:
            diff[t] += p
            diff[f] -= p

        occupancy = 0
        for p in diff:
            occupancy += p
            if occupancy > capacity: return False

        return True
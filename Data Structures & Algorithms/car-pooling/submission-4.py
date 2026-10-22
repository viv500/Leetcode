class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda s: s[1])
        occupancy = 0
        end_times = []

        for people, start, end in trips:
            while end_times and end_times[0][0] <= start:
                _, dropped_off = heapq.heappop(end_times)
                occupancy -= dropped_off

            occupancy += people
            heapq.heappush(end_times, (end, people))
            
            if occupancy > capacity: return False


        return True
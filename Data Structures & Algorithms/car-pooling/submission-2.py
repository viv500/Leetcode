import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = []
        
        occupancy = 0

        for passenger_count, frm, to in trips:
            heapq.heappush(minHeap, (to, passenger_count))
            while minHeap and minHeap[0][0] <= frm:
                occupancy -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            occupancy += passenger_count

            if occupancy > capacity: return False

        return True


import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        minHeap = [(t[2], t[0]) for t in trips]
        heapq.heapify(minHeap)

        occupancy = 0

        for passenger_count, frm, to in trips:
            while minHeap and minHeap[0][0] <= frm:
                occupancy -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            occupancy += passenger_count

            if occupancy > capacity: return False

        return True


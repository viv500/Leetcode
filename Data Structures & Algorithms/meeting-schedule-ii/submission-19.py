"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda s: (s.start, s.end))
        minHeap = []

        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval.end)

        return len(minHeap)
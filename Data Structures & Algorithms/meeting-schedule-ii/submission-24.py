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
        endTimes = []
        intervals.sort(key = lambda i: i.start)

        for interval in intervals:
            start, end = interval.start, interval.end
            if endTimes and endTimes[0] <= start:
                heapq.heappop(endTimes)
            
            heapq.heappush(endTimes, end)

        return len(endTimes)
        
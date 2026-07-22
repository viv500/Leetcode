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
        intervals.sort(key = lambda x: x.start)
        end_times = []

        for interval in intervals:
            start, end = interval.start, interval.end

            if end_times and end_times[0] <= start:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, end)

        return len(end_times)
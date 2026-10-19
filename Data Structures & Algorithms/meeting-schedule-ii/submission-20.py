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
        intervals.sort(key = lambda s: s.start)
        end_times = []

        for i in intervals:
            if end_times and i.start >= end_times[0]:
                heapq.heappop(end_times)
            
            heapq.heappush(end_times, i.end)

        return len(end_times)
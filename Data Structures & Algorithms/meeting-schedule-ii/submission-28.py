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
        intervals.sort(key = lambda i: i.start)
        end = []

        for i in intervals:
            if end and i.start >= end[0]:
                heapq.heappop(end)

            heapq.heappush(end, i.end)

        return len(end)
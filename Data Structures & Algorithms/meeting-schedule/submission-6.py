"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda s: s.start)

        prev_start, prev_end = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            if start < prev_end:
                return False
            prev_start, prev_end = start, end

        return True
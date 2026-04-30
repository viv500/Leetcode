"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 2 pointer approach
        # intuition: start with rooms = 0
        # start < end can but does not always imply overlap
        # it could also be the start and end of the same interval, in which case, 1 room still needs to be used!

        start = []
        end = []
        rooms = 0
        max_rooms = 0

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        i, j = 0, 0

        while i < len(start) and j < len(end):
            # end >= start is no overlap, so 1 less room
            if start[i] < end[j]:
                rooms += 1
                i += 1
            else:
                rooms -= 1
                j += 1
            
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms




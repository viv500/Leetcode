class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy approach
        # sort intervals by increasing start times and if overlaps are found, greedily remove the one
        # that has the latest finish time
        # this opens up slots the same or more time for future intervals
        if not intervals: return 0

        intervals.sort()
        cur_end = intervals[0][1]
        remove_count = 0

        for start, end in intervals[1:]:
            # there's overlap
            if start < cur_end:
                remove_count += 1
                # set current end to be earliest end
                cur_end = min(cur_end, end)
            
            # no overlap, only 1 end
            else:
                cur_end = end

        return remove_count


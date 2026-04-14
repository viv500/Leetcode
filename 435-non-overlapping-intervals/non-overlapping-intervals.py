class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy approach: sort intervals by increaseing start times
        # then get rid of overlaps by greedily removing the interval that ends first
        # stack could be good for visualization but not needed
        intervals.sort()
        remove_count = 0
        cur_end = intervals[0][1]

        for start,end in intervals[1:]:
            # is their overlap?
            if start < cur_end:
                remove_count += 1
                cur_end = min(cur_end, end)
            else:
                cur_end = end

        return remove_count
            
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # append new interval, sort, merge interval algorithm

        intervals.append(newInterval)
        intervals.sort()

        output = []
        cur_start = intervals[0][0]
        cur_end = intervals[0][1]

        print(intervals)

        for next_start,next_end in intervals[1:]:
            # overlap?
            if next_start <= cur_end:
                cur_end = max(cur_end, next_end)
            else:
                output.append([cur_start, cur_end])
                cur_start = next_start
                cur_end = next_end

        output.append([cur_start, cur_end])


        return output

        
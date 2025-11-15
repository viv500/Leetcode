class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # have pointer for start and end. keep moving end as long as theres a valid overlap. no more overlaps? add [start, end] to array and increment pointers
        
        intervals.sort()
        output = []

        cur_start = intervals[0][0]
        cur_end = intervals[0][1]

        for interval in intervals[1:]: # start with second one
            if interval[1] > cur_end and interval[0] <= cur_end:
                cur_end = interval[1]
            elif interval[1] <= cur_end:
                continue
            else:
                output.append([cur_start, cur_end])
                cur_start = interval[0] #modify pointers, we're done with the previous interval
                cur_end = interval[1]

        output.append([cur_start, cur_end]) # last one gets skipped

        return output

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []

        cur_start, cur_end = intervals[0][0], intervals[0][1]

        for start, end in intervals[1:]:
            if cur_end >= start:
                cur_end = max(cur_end, end)
            else:
                output.append([cur_start, cur_end])
                cur_start, cur_end = start, end
        
        output.append([cur_start, cur_end])
        return output
        
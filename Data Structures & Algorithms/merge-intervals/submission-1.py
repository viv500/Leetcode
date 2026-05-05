class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []

        cur_start, cur_end = intervals[0]

        for interval in intervals[1:]:
            next_start, next_end = interval[0], interval[1]

            if next_start <= cur_end:
               cur_end = max(cur_end, next_end)
            else:
                output.append([cur_start, cur_end])
                cur_start, cur_end = next_start, next_end
        
        output.append([cur_start, cur_end])
        return output

            
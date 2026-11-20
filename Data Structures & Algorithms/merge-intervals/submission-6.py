class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= prev_end:
                prev_end = max(prev_end, end)
            else:
                result.append([prev_start, prev_end])
                prev_start, prev_end = start, end

        result.append([prev_start, prev_end])

        return result
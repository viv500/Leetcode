class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        result = []
        start, end = newInterval

        # pre merging
        while index < len(intervals) and intervals[index][1] < start:
            result.append(intervals[index])
            index += 1

        while index < len(intervals) and end >= intervals[index][0]:
            start = min(start, intervals[index][0])
            end = max(end, intervals[index][1])
            index += 1

        result.append([start, end])

        while index < len(intervals):
            result.append(intervals[index])
            index += 1
        return result

        

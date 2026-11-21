class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        index = 0
        result = []

        new_start, new_end = newInterval

        while index < len(intervals) and new_start > intervals[index][1]:
            result.append(intervals[index])
            index += 1

        while index < len(intervals) and new_end >= intervals[index][0]:
            new_end = max(new_end, intervals[index][1])
            new_start = min(new_start, intervals[index][0])
            index += 1
        
        result.append([new_start, new_end])

        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result
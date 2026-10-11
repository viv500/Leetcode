class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        index = 0
        new_start, new_end = newInterval
        while index < len(intervals) and intervals[index][1] < new_start:
            result.append([intervals[index][0], intervals[index][1]])
            index += 1
        
        while index < len(intervals) and new_end >= intervals[index][0]:
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1
        
        result.append([new_start, new_end])

        while index < len(intervals):
            result.append([intervals[index][0], intervals[index][1]])
            index += 1

        return result
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        index = 0
        new_start, new_end = newInterval
        n = len(intervals)

        while index < n and intervals[index][1] < new_start:
            output.append(intervals[index])
            index += 1

        # at this point, we either got to the end or theres overlap

        while index < n and intervals[index][0] <= new_end and intervals[index][1] >= new_start:
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1
        output.append([new_start, new_end])

        while index < n:
            output.append(intervals[index])
            index += 1

        return output

        
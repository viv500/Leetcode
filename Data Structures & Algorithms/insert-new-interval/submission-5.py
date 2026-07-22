class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        new_start, new_end = newInterval
        output = []

        while index < len(intervals) and intervals[index][1] < new_start:
            output.append(intervals[index])
            index += 1
        print(output)

        while index < len(intervals) and intervals[index][0] <= new_end:
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1

        output.append([new_start, new_end])
        print(output)


        while index < len(intervals):
            output.append(intervals[index])
            index += 1
        
        print(output)

        return output



        

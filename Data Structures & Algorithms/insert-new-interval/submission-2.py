class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is already sorted by start time

        # 3 step process

        # 1. add all intervals that have no overlap with newInterval
        # 2. handle all the merge logic
        # 3. add the remaining intervals

        output = []
        new_start, new_end = newInterval
        index = 0
        n = len(intervals)

        # step 1
        while index < n and intervals[index][1] < new_start:
            output.append(intervals[index])
            index += 1

        # step 2
        while index < n and new_end >= intervals[index][0]: # and implicitly, intervals[index][1] >= new_start
            # these 2 ANDS are needed to handle merges from both left and right
            new_start = min(new_start, intervals[index][0])
            new_end = max(new_end, intervals[index][1])
            index += 1
        
        output.append([new_start, new_end]) # this works even if no merging needed to be done


        # step 3
        while index < len(intervals):
            output.append(intervals[index])
            index += 1
        
        return output
        

            
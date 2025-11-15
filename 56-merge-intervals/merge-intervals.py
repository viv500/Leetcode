class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # have pointer for start and end. keep moving end as long as theres a valid overlap. no more overlaps? add [start, end] to array and increment pointers


        def mergesort(array):
            if len(array) <= 1:
                return array
    
            mid = len(array) // 2
            left_array = array[:mid]
            right_array = array[mid:]

            mergesort(left_array)
            mergesort(right_array)

            i = j = k = 0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j += 1
                k += 1

            while i < len(left_array):
                array[k] = left_array[i]
                i += 1
                k += 1

            while j < len(right_array):
                array[k] = right_array[j]
                j += 1
                k += 1


        mergesort(intervals)

        output = []

        cur_start = intervals[0][0]
        cur_end = intervals[0][1]


        # more consisely, 
        # if interval[0] <= cur_end::
        #       cur_end = max(cur_end, interval[1])
        # no need for elif anymore
        for interval in intervals[1:]: # start with second one
            if interval[1] > cur_end and interval[0] <= cur_end:
                cur_end = interval[1]
            elif interval[1] <= cur_end: # need this condition incase interval is fully contained or a subset of the cur interval
                continue
            else:
                output.append([cur_start, cur_end])
                cur_start = interval[0] #modify pointers, we're done with the previous interval
                cur_end = interval[1]

        output.append([cur_start, cur_end]) # last one gets skipped

        return output

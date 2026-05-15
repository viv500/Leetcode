import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force: iterate through intervals for each query : O(m * n)

        # sorting both helps us iterate through intervals and pop items from minHeap if a query isnt in it, since we are
        # GUARENTEED that future points wont be in the query range either
        # note: point interval has length 1 ex. [4,4]

        intervals.sort() 
        minHeap = []
        result = {} # need to map sorted order values ot original values so we can put the query results back into its original order
        i = 0


        for query in sorted(queries):

            # add all 
            while i < len(intervals) and intervals[i][0] <= query: # if this is true, then the interval HAS to contain the point
                # length is the main factor, then for tie breaker, earliest ending time. we wanna consume the earlier intervals now so later queries can user later intervals
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (length, intervals[i][1]))
                i += 1

            # pop intervals that don't fit in the range
            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            # now, we are guarenteed to have the smallest length interval containing query IF the minHeap isn't empty
            result[query] = minHeap[0][0] if minHeap else -1

        return [result[query] for query in queries]

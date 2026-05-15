import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Brute force: O(n*m). Better: sort both + min heap by interval length.

        # Process queries in sorted order. For each query:
        # - push all intervals starting <= query (they potentially contain it)
        # - pop intervals ending < query (they definitely don't contain it)
        # - heap top is the smallest valid interval, if any

        # result dict maps query value -> answer, to restore original query order at the end
        
        intervals.sort()
        minHeap = []
        result = {}
        i = 0

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (length, intervals[i][1]))
                i += 1

            while minHeap and minHeap[0][1] < query:
                heapq.heappop(minHeap)

            result[query] = minHeap[0][0] if minHeap else -1

        return [result[q] for q in queries]
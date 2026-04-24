import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # (O(n log k))
        minHeap = []
        for num in nums:
            if len(minHeap) == k:
                if num > minHeap[0]:
                    heapq.heappop(minHeap)
                else:
                    continue
            heapq.heappush(minHeap, num)

        return minHeap[0]

       
       # solution with sorting -> O(n log n)
       # nums.sort(reverse=True)
       # return nums[k - 1]
        
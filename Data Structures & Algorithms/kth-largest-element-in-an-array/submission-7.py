class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []

        for num in nums:
            heapq.heappush(largest, num)
            if len(largest) > k: heapq.heappop(largest)

        return largest[0]
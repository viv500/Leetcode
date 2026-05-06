import heapq
class MedianFinder:
    # 2 heaps
    # max heap to represent first half of sorted order, min heap to represent second half
    # done this way so we can have access to the elements closest to the middle ex. 1 2 ; 3 4
    # try keeping these heaps approx the same length

    # when finding median, heap with larger size has the median element at its peak
    # if both have the same size, its the average

    # insertion logic:
    #   by default, always add to the max heap. if theres a difference in lengths of over 1, pop the largest from max
    #   and add it to the min
    # this ensures 2 invariants
    #      1. maxheap[0] <= minheap[0]
    #      2. len(maxheap) approx. = len(minheap)

    def __init__(self):
        self.minHeap_right = []
        self.maxHeap_left = []

    def addNum(self, num: int) -> None:
        # add it to left by default, if overflow, transfer number to right
        heapq.heappush_max(self.maxHeap_left, num)

        m, n = len(self.minHeap_right), len(self.maxHeap_left)

        # invariant 1. maxheap[0] <= minheap[0] (only pop left cuz thats where we inserted)
        if (m > 0 and n > 0 and self.maxHeap_left[0] > self.minHeap_right[0]):
            transfer = heapq.heappop_max(self.maxHeap_left)
            heapq.heappush(self.minHeap_right, transfer)

            n -= 1
            m += 1

        # invariant 2. len(maxheap) approx. = len(minheap)
        if n - m > 1:
            transfer = heapq.heappop_max(self.maxHeap_left)
            heapq.heappush(self.minHeap_right, transfer)
        elif m - n > 1:
            transfer = heapq.heappop(self.minHeap_right)
            heapq.heappush_max(self.maxHeap_left, transfer)


    def findMedian(self) -> float:
        print("left:", self.maxHeap_left, "right:", self.minHeap_right)
        m, n = len(self.minHeap_right), len(self.maxHeap_left)

        if m > n:
            return self.minHeap_right[0]

        elif m < n:
            return self.maxHeap_left[0]

        else:
            return (self.minHeap_right[0] + self.maxHeap_left[0]) / 2

    
        
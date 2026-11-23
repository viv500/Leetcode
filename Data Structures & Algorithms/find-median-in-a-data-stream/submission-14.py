import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

        

    def addNum(self, num: int) -> None:
        l, r = self.left, self.right
        heapq.heappush_max(l, num)

        if l and r and l[0] > r[0]:
            num = heapq.heappop_max(l)
            heapq.heappush(r, num)

        if len(l) - len(r) >= 2:
            num = heapq.heappop_max(l)
            heapq.heappush(r, num)

        elif len(r) - len(l) >= 2:
            num = heapq.heappop(r)
            heapq.heappush_max(l, num)

        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]
        
        
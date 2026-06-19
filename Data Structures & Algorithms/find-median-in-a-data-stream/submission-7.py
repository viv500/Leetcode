import heapq
class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.lower, num)

        # invariant logic
        if self.lower and self.upper and self.lower[0] > self.upper[0]:
            value = heapq.heappop_max(self.lower)
            heapq.heappush(self.upper, value)

        # rebalancing logic
        if len(self.lower) - len(self.upper) > 1:
            value = heapq.heappop_max(self.lower)
            heapq.heappush(self.upper, value)
        elif len(self.upper) - len(self.lower) > 1:
            value = heapq.heappop(self.upper)
            heapq.heappush_max(self.lower, value)

        
        print("lower: ", self.lower)
        print("upper: ", self.upper)
        
    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        elif len(self.lower) < len(self.upper):
            return self.upper[0]
        else: return (self.lower[0] + self.upper[0]) / 2
        
        
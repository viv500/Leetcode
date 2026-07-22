import heapq
class MedianFinder:

    def __init__(self):
        self.smaller = []
        self.bigger = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.smaller, num)

        # bigger smaller invariant
        while self.smaller and self.bigger and self.smaller[0] > self.bigger[0]:
            val = heapq.heappop_max(self.smaller)
            heapq.heappush(self.bigger, val)

        print(self.smaller)
        print(self.bigger)

        # size invariant
        while len(self.smaller) - len(self.bigger) > 1:
            val = heapq.heappop_max(self.smaller)
            heapq.heappush(self.bigger, val)

        while len(self.bigger) - len(self.smaller) > 1:
            val = heapq.heappop(self.bigger)
            heapq.heappush_max(self.smaller, val)

        

    def findMedian(self) -> float:
        small_size, big_size = len(self.smaller), len(self.bigger)
        if small_size > big_size:
            return self.smaller[0]
        elif big_size > small_size:
            return self.bigger[0]
        else:
            return (self.smaller[0] + self.bigger[0]) / 2
        
        
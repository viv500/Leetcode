class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        low, high = self.low, self.high
        heapq.heappush_max(low, num)

        # low < high constraint
        if low and high and low[0] > high[0]:
            low_val = heapq.heappop_max(low)
            heapq.heappush(high, low_val)

        # low bigger
        if len(low) - len(high) > 1:
            low_val = heapq.heappop_max(low)
            heapq.heappush(high, low_val)

        # high bigger
        if len(high) - len(low) > 1:
            high_val = heapq.heappop(high)
            heapq.heappush_max(low, high_val)
        

    def findMedian(self) -> float:
        low, high = self.low, self.high

        if len(low) > len(high):
            return low[0]
        elif len(high) > len(low):
            return high[0]
        else:
            return (low[0] + high[0]) /2
        
        
import bisect
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.timemap = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))    

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        low, high = 0, len(values) - 1
        value = ""

        while low <= high:
            mid = (low + high) // 2
            time = values[mid][0]

            if time <= timestamp:
                value = values[mid][1]
                low = mid + 1
            else: 
                high = mid - 1

        return value


        

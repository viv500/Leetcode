from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
    
        values = self.store[key]
        low, high = 0, len(values) - 1

        val = ""
        while low <= high:
            mid = (low + high) // 2
            t = values[mid][1]

            if t <= timestamp:
                val = values[mid][0]
                low = mid + 1
            else:
                high = mid - 1


        return val
        

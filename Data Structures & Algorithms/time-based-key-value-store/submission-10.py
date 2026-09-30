from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        store = self.store[key]
        value = ""

        start, end = 0, len(store) - 1

        while start <= end:
            mid = (start + end) // 2
            if store[mid][1] <= timestamp: 
                value = store[mid][0]
                start = mid + 1
            else: end = mid - 1

        return value

        

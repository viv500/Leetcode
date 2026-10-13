from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])  

    def get(self, key: str, timestamp: int) -> str:
        key_store = self.store[key]
        low, high = 0, len(key_store) - 1
        value = ""

        while low <= high:
            mid = (low + high) // 2

            if key_store[mid][0] <= timestamp:
                value = key_store[mid][1] 
                low = mid + 1
            else:
                high = mid - 1


        return value


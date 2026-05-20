from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        print(self.store)


    def get(self, key: str, timestamp: int) -> str:
        store = self.store[key]
        value = ""

        low, high = 0, len(store) - 1

        while low <= high:
            mid = (low + high) // 2
            prev_timestamp = store[mid][0]

            if prev_timestamp <= timestamp:
                value = store[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return value

        

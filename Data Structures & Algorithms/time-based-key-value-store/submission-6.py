from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        print(self.store)
        values = self.store.get(key, [])
        if len(values) == 0: return ""
        if len(values) == 1: return values[0][0] if values[0][1] <= timestamp else ""

        # binary sarch (for largest value smaller than timestamp)
        low = 0
        high = len(values) - 1
        prev_timestamp = values[0][1]
        while low <= high:
            mid = (high + low) // 2

            prev_timestamp = values[mid][1]
            prev_value = values[mid][0]

            if prev_timestamp <= timestamp:
                low = mid + 1
            else:
                high = mid - 1

        # when the alg ends, high is exactly 1 smaller than the target timestamp (mid - 1)
        # mid was always valid, as soon as it goes invalid (the else), "high" is the last valid state
        prev_timestamp = values[high][1]
        prev_value = values[high][0]

        return prev_value if prev_timestamp <= timestamp else ""

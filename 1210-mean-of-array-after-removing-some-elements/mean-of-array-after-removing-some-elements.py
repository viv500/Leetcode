class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr.sort()
        to_remove = int(0.05 * len(arr))

        return sum(arr[to_remove:(len(arr) - to_remove)])/(len(arr) - (2 * to_remove))
        
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        cur_max = arrays[0][-1]
        cur_min = arrays[0][0]
        result = 0

        length = len(arrays)

        # cuz we've already visited the first array
        for i in range(1, length):
            arr = arrays[i]

            # compaing current result to 1) this lists max - current min 2) current max - this lists min
            result = max(result, arr[-1] - cur_min, cur_max - arr[0])

            cur_min = min(arr[0], cur_min)
            cur_max = max(arr[-1], cur_max)

        return result


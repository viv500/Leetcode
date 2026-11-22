from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxx = deque()

        for i, n in enumerate(nums):
            while maxx and maxx[-1][1] < n:
                maxx.pop()

            if maxx and maxx[0][0] <= (i - k):
                maxx.popleft()

            maxx.append((i, n))

            if i - k + 1 >= 0:
                result.append(maxx[0][1])

        return result

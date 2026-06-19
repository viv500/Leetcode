from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # monotically decreasing deque
        # pop from the left when out of bounds, add 
        q = deque()
        output = []

        for index, num in enumerate(nums):
            if q and q[0][1] < index - k + 1:
                q.popleft()

            # insertion - if any number to the left of current num is less, theres no future window where it can help
            # so we can remove it (from right to left)
            while q and q[-1][0] < num:
                q.pop()

            q.append((num, index))

            # only append after first window is created
            if index >= k - 1: output.append(q[0][0])

        return output

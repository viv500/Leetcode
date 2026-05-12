from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force checking each window is O(k * (n - k))
        """
        Monotonic decreasing deque — O(n) time, O(k) space.
        Each element is enqueued and dequeued at most once.
        Stores indices (not values) to detect out-of-bounds elements.
        """
        q = deque()  # indices, front = current window max
        output = []

        for i, num in enumerate(nums):
            # Evict index if it's outside the current window [i-k+1, i]
            if q and q[0] < i - k + 1:
                q.popleft()

            # Maintain decreasing order — pop smaller elements from the back
            # (they can never be the max while num is still in the window)
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            # Emit max once the first full window is formed
            if i + 1 >= k: output.append(nums[q[0]])

        return output
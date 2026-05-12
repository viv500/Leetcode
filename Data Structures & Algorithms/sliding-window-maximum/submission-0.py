from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # check each window - O(n * (k - n)) time

        # mmonotonic decreasing queue solution
        # O (n) time
        # each element enters and exits the queue exactly once -> O(n)
        # !! NOTE !! why deque? since we left element goes out of bounds and right comes in, we need an efficicent way to
        # both popleft() and popright()

        # !! NOTE !! q stores indices not values! this allows us to move items out of th queue if out of bounds

        q = deque()
        output = []

        for i in range(len(nums)): # i is the position of the new element entering the sliding door (at the start, the initial window elements)

            # removing out of bounds characters
            while q and q[0] < i - k + 1: # left boundary
                q.popleft()

            # forgetting any lower values (they can't possibly be max in the future, since the high value is infront)
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # add new element to the window
            q.append(i)

            # largest element (leftmost) in monotonic decreasing queue
            if i + 2 > k: output.append(nums[q[0]])

        return output

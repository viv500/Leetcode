from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # queue is monotonically decreasing
        window = deque()
        output = []

        for i in range(len(nums)):
            # remove numbers that are outside window
            if window and window[0] < i - k + 1:
                window.popleft()

            # if theres larger number, we can remove any previous smaller nummer since larger will always be ahead
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)

            # only add to result if window is at least size k
            if i + 1 >= k: output.append(nums[window[0]])

        return output

            


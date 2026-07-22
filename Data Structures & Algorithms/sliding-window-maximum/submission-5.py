from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            while q and q[0] < i - k + 1:
                q.popleft()
            
            q.append(i)


            if i - k + 1 >= 0:
                result.append(nums[q[0]])
        
        return result
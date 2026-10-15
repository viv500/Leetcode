import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = list(Counter(tasks).values())
        heapq.heapify_max(maxHeap)

        cooldown = deque()
        time = 0
        while maxHeap or cooldown:

            if maxHeap:
                task = heapq.heappop_max(maxHeap)
                if task - 1 > 0: cooldown.append((time + n, task - 1))

            if cooldown and time >= cooldown[0][0]:
                _, task = cooldown.popleft()
                heapq.heappush_max(maxHeap, task)
            
            time += 1

        return time




        
from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = list(Counter(tasks).values())
        heapq.heapify_max(tasks)
        cool = deque()
        time = 0

        while tasks or cool:
            if tasks:
                count = heapq.heappop_max(tasks)
                count -= 1
                if count > 0: cool.append((count, time + n))

            if cool and time >= cool[0][1]:
                count, _ = cool.popleft()
                heapq.heappush_max(tasks, count)

            time += 1


        return time

        
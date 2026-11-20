from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count = list(count.values())
        heapq.heapify_max(count)
        cool = deque()
        time = 0

        while count or cool:
            if count:
                c = heapq.heappop_max(count)
                c -= 1
                if c > 0: cool.append((c, time + n))

            if cool and time >= cool[0][1]:
                c, _ = cool.popleft()
                heapq.heappush_max(count, c)

            time += 1

        return time

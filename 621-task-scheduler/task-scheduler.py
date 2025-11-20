import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks, n):
        # max_heap: greedily finishing the highest occurance character tasks
        # queue: stores [time the task can be done again, -count] i.e cooldown
        # python only has min heap so store vals as negative to create max heap

        # max heap only stores counts. cooldown stores (count, time at which we can rerun)

        tasks = Counter(tasks)
        cooldown = deque()
        max_heap = [-count for count in tasks.values()]
        heapq.heapify(max_heap) # turn this into a max heap
        time = 0

        while(max_heap or cooldown):
            time += 1
            if max_heap: # theres elements to be added to cooldown
                count = -heapq.heappop(max_heap) - 1 # calculates how many left

                if count > 0: # only add to cooldown if theres more of this task
                    cooldown.append([time + n, count])

            if cooldown and cooldown[0][0] == time: # the task is now ready!
                heapq.heappush(max_heap, -cooldown.popleft()[1]) # need to negate this count

        return time

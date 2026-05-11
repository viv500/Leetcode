from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # time: O(n)
        # maxHeap:
        # used to greedily schedule the most frequently occuring task first -> works out to be optimal
        # also since there are only 26 characters in the alphabet, pusing and popping are O(log 26) = O(log 1)

        # queue:
        # used to find the task is now available after cooldown. since time is incremented every iteration, and heap is
        # FIFO, naturally the task thats availale first is scheduled

        # note: the queue simply holds counts and times, it doesnt decrement count
        # only the max heap "schedules" tasks and can decrement count

        cnt = Counter(tasks)
        maxHeap = list(cnt.values())
        heapq.heapify_max(maxHeap) # we only care about the counts, not the actual characters
        time = 0
        cooldown_q = deque() # pairs of (count, idle_time)

        while maxHeap or cooldown_q:
            time += 1

            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                if count - 1 > 0: # dont want to push tasks with 0 count to the q
                    cooldown_q.append((count - 1, time + n)) # it will be avaiable at time + n
            
            if cooldown_q and time >= cooldown_q[0][1]: # schedule if any task has finished its cool down
                heapq.heappush_max(maxHeap, cooldown_q.popleft()[0]) # pushing the count without decrementing
        
        return time




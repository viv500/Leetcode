class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # min heap: stores [processing time, index] -> this ensures smallest time task is selected and ties are broken by smaller index
        # heap doesnt need info about enque time since it is only added to the heap when its ready to run (enque time met)
        # sort the tasks by enque time
        # min heap stores tasks that area ready (time constraint)

        for index, task in enumerate(tasks):
            task.append(index)

        # sort by enque time
        tasks.sort(key = lambda t : t[0])

        print(tasks)

        output, minheap = [], []
        # output = minheap = [] IS NOT THE SAME, lists are mutable so they will share mutations
        # for a = b = 0, a new object will be created for any mutation

        i, time = 0, tasks[0][0] # we want to start when the earliest task is ready to start

        # if there are tasks ready to be processed/ not yet ready and are yet to be added to the heap
        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:

                # taks can be added to heap
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]]) # [processing time, index]
                i += 1
            
            # no tasks meet time, fast forward to next earliest time
            if not minheap: # i.e. if loop started due to i < len(tasks)
                time = tasks[i][0]
            else: # tasks are ready to run, pick the smallest one
                proc_time, index = heapq.heappop(minheap)

                output.append(index)
                time += proc_time

        return output


        
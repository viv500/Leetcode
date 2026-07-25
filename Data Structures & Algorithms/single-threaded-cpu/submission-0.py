
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # add index so we dont use ordering info
        for index, task in enumerate(tasks):
            task += [index]

        print(tasks)

        # sort by processing time so we can go through the array in order
        tasks.sort()
        task_index = 0
        print(tasks)

        time = 0
        output = []
        minHeap = []

        while len(output) < len(tasks):
            # add all available tasks to minHeap
            while task_index < len(tasks) and tasks[task_index][0] <= time:
                # add the processing time and index to the heap
                heapq.heappush(minHeap, (tasks[task_index][1], tasks[task_index][2]))
                task_index += 1

            # pop the task with least processing time
            if minHeap:
                next_task_time, next_task_index = heapq.heappop(minHeap)
                output.append(next_task_index)
                time += next_task_time
            else: time += 1

        return output

        
        
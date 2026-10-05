from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        graph = defaultdict(list)
        time = [0] * len(manager)
        
        for employee in range(len(manager)):
            mgr = manager[employee]
            if mgr != -1:
                graph[mgr].append((informTime[mgr], employee))

        def dfs(employee):
            for cost, nei in graph[employee]:
                time[nei] = (time[employee] + cost)
                dfs(nei)
            
            return

        dfs(headID)
        return max(time)
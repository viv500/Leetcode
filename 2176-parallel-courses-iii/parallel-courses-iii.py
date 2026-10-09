from collections import defaultdict
class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)

        for u, v in relations:
            graph[u].append(v)

        max_time = {}
        def dfs(i):

            if i in max_time: return max_time[i]

            maxx = time[i - 1]
            for nei in graph[i]:
                maxx = max(maxx, dfs(nei) + time[i - 1])

            max_time[i] = maxx
            return max_time[i]

        times = []
        for i in range(1, n + 1):
            times.append(dfs(i))

        return max(times)

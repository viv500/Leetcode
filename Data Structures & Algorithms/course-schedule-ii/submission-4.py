from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        state = [0] * numCourses
        order = []

        def dfs(course):
            if state[course] == 2: return True
            if state[course] == 1: return False

            state[course] = 1
            for nei in graph[course]:
                if not dfs(nei): return False

            state[course] = 2
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return order

        
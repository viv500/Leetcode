from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        states = [0] * numCourses
        graph = defaultdict(list)
        result = []

        for u, v in prerequisites:
            graph[u].append(v)

        def dfs(course):
            if states[course] == 1: return False
            if states[course] == 2: return True

            states[course] = 1
            for nei in graph[course]:
                if not dfs(nei): return False

            states[course] = 2
            result.append(course)
            return True


        for course in range(numCourses):
            if not dfs(course): return []

        return result
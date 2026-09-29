from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        leads_to = defaultdict(list)
        state = [0] * numCourses

        for u, v in prerequisites:
            leads_to[u].append(v)

        def bfs(course):
            if state[course] == 1: return False
            if state[course] == 2: return True

            state[course] = 1

            for c in leads_to[course]:
                if not bfs(c): return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not bfs(course): return False

        return True


        
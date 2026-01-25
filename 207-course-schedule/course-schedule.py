from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        leads_to = defaultdict(list)
        states = numCourses * [0]

        for second, first in prerequisites:
            leads_to[first].append(second)

        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True

            states[course] = 1

            for lead in leads_to[course]:
                if not dfs(lead):
                    return False

            states[course] = 2

            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False


        return True
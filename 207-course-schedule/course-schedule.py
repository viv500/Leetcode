from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        leads_to = defaultdict(list)
        for course, lead_to in prerequisites:
            leads_to[course].append(lead_to)

        states = [0] * numCourses

        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True

            states[course] = 1

            for lead_to in leads_to[course]:
                if not dfs(lead_to):
                    return False

            states[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
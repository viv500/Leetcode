from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        states = [0] * numCourses
        prereq_to_course = defaultdict(list)
        courseList = []

        for course, leads_to in prerequisites:
            prereq_to_course[course].append(leads_to)


        def dfs(course):
            if states[course] == 2: return True
            if states[course] == 1: return False

            states[course] = 1

            for leads_to in prereq_to_course[course]:
                if not dfs(leads_to):
                    return False

            states[course] = 2
            courseList.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []

        return courseList
unvisited = 0
visiting = 1
visited = 2

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(list)
        for course, leads_to in prerequisites:
            course_map[course].append(leads_to)

        state = [0] * numCourses
        courseList = []

        def dfs(course):
            if state[course] == visiting: return False
            if state[course] == visited: return True

            state[course] = visiting

            for nei in course_map[course]:
                if not dfs(nei): return False

            state[course] = visited
            courseList.append(course)

            return True

        
        for course in range(numCourses):
            if not dfs(course): return []

        return courseList
        
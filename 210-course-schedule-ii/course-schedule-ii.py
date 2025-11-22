from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        leads_to = defaultdict(list)
        output = []

        for course, lead_to in prerequisites:
            leads_to[course].append(lead_to)

        states = [0] * numCourses
        visited = 2
        visiting = 1
        unvisited = 0

        def dfs(course):
            if states[course] == visited:
                return True
            if states[course] == visiting:
                return False

            states[course] = visiting

            for courses in leads_to[course]:
                if not dfs(courses):
                    return False

            states[course] = visited
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []


        return output


        
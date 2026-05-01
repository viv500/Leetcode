from collections import defaultdict
UNVISITED = 0
VISITING = 1
VISITED = 2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for course, leads_to in prerequisites:
            courses[course].append(leads_to)

        print(courses)
        visited = [0] * numCourses


        def dfs(course):
            if visited[course] == VISITING: return False
            if visited[course] == VISITED: return True

            # else, = UNVISITED
            visited[course] = VISITING
            for leads_to in courses[course]:
                if not dfs(leads_to): return False

            visited[course] = VISITED

            return True


        
        for course in range(numCourses):
            if not dfs(course): return False

        
        return True

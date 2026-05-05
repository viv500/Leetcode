from collections import defaultdict

UNVISITED = 0
VISITING = 1
VISITED = 2

# in a dfs, a node is in "visiting" state until all its neighbours are recursively explored
# if the node is found "visiting" in its dfs, then there must've been a loop in the graph
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

            # need this retrun True! if not, function returns None which triggers "if not dfs()"
            return True


        
        for course in range(numCourses):
            if not dfs(course): return False

        
        return True

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = defaultdict(list)

        for prereq, leads_to in prerequisites:
            graph[prereq].append(leads_to)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED:
                return True
            elif states[node] == VISITING:
                return False

            
            # we are now visiting
            states[node] = VISITING

            for leads_to in graph[node]:
                if not dfs(leads_to):
                    return False

            # everything went okay and we're back to the original course
            states[node] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
    


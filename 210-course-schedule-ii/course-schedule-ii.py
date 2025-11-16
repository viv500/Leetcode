from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # topological sort !!

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        graph = defaultdict(list)

        for prereq, leads_to in prerequisites:
            graph[prereq].append(leads_to)

        topo_order = []

        def dfs(course):
            state = states[course]

            if state == VISITING:
                return False
            elif state == VISITED:
                return True

            states[course] = VISITING

            for leads_to in graph[course]:
                if not dfs(leads_to):
                    return False

            # the first course to reach this is the one with the least dependancies
            # others are sitll in nested recursive calls
            # adding courses here will preserve topoligcal order

            states[course] = VISITED
            topo_order.append(course)

            # to tell dfs that dependancies are resolved
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []

        # by this point, all courses can be taken
        return topo_order
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # [course, prereq]
        # [1, 0] [0, 1]

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        leads = defaultdict(list)

        for leads_to, prereq in prerequisites:
            leads[prereq].append(leads_to)

        def dfs(course):
            if states[course] == VISITING:
                return False
            if states[course] == VISITED:
                return True

            # must be unvisited
            states[course] = VISITING

            # visit all the coruses that this course leads to
            for lead in leads[course]:
                if not dfs(lead):
                    return False

            
            states[course] = VISITED

            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True



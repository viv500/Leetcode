from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # dfs approach:
        # build adjacency matrix with course -> leads to format. call dfs on each course that goes deep into the "leads to" chain
        # if it finds a vertex its "visiting" -> cycle. if "visited" -> good to go return true. if not visited, mark as visiting.
        # once we call dfs on all its neighbours (leads to courses) and everything works fine, mark it as visited and return true

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * (numCourses)

        leads = defaultdict(list) # if we try to access an element that doesnt exist, it creates an empty list value for that key

        for leads_to, prereq in prerequisites:
            leads[prereq].append(leads_to)

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING: # cycle found
                return False        

            # its an unvisited node!
            states[node] = VISITING

            for leads_to in leads[node]:
                if not dfs(leads_to):
                    return False
            
            # no neighbours form a cycle
            states[node] = VISITED

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        leads_to = defaultdict(list)

        # adjacency hashmap mapping course -> course it leads to
        for course, prereq in prerequisites:
            leads_to[prereq].append(course)

        unvisited, visiting, visited = 0, 1, 2
        # if a node is "visited", its prereqs have been resolved 
        # if its in "visiting" we are currently resolving its prereq and leads to chain, if we rediscover a "visiting" node, there
        # is a cycle in its dependancies

        # the state of courses
        states = [unvisited] * numCourses


        def dfs(course):
            if states[course] == 2:
                return True
            if states[course] == 1:
                return False

            # add to visiting
            states[course] = 1

            for lead_to in leads_to[course]:
                # if any returns false, cycle in depednancies. if true, we can continue checking
                if not dfs(lead_to):
                    return False

            # all dependancies resolved
            states[course] = 2

            return True # need this or python my implicitly return 0 (False)


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
                
            

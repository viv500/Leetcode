from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        state = [0] * numCourses
        order = []

        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(course):
            if state[course] == 1: return False
            if state[course] == 2: return True

            state[course] = 1
            for nei in graph[course]:
                if not dfs(nei): return False

            order.append(course)
            state[course] = 2
    
            return True

        for course in range(numCourses):
            if not dfs(course): return []

        return order

        

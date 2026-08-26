from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        graph = defaultdict(list)
        output = []
        for u, v in tickets:
            graph[u].append(v)

        def dfs(location):
            while graph[location]:
                dfs(graph[location].pop())

            output.append(location)

        dfs("JFK")
        return output[::-1]
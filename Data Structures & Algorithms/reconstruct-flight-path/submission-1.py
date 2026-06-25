from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        output = []
        graph = defaultdict(list)

        for to, fro in sorted(tickets, reverse=True):
            graph[to].append(fro)


        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            output.append(node)

        dfs("JFK")
        return output[::-1]
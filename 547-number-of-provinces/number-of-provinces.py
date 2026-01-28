class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_count = 0
        visited = [0] * len(isConnected)

        def dfs(city):
            if visited[city] == 1:
                return

            visited[city] = 1
            for nei, connected in enumerate(isConnected[city]):
                if connected == 1:
                    dfs(nei)
                    visited[nei] = 1

        for city in range(len(isConnected)):
            if visited[city] == 0:
                province_count += 1
                dfs(city)

        return province_count
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        province_count = 0

        def dfs(main_city):
            # all cities in isConnected[i] are cities that city i is connected to
            for city, is_connected in enumerate(isConnected[main_city]):
                if(is_connected and city not in visited):
                    visited.add(city)
                    dfs(city)

        for city in range(len(isConnected)):
            if city not in visited:
                province_count += 1
                dfs(city)

        return province_count

        


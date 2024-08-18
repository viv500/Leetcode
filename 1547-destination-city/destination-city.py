class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        froms = set()
        tos = set()

        for cities in paths:
            froms.add(cities[0])
            tos.add(cities[1])
        

        for city in tos:
            if city not in froms:
                return city
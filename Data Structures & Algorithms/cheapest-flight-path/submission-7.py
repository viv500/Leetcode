class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf") for _ in range(n)]
        distance[src] = 0

        for _ in range(k + 1):
            copy_distance = distance[:]
            for fromm, to, price in flights:
                copy_distance[to] = min(copy_distance[to], distance[fromm] + price)
            
            distance = copy_distance

        return distance[dst] if distance[dst] != float("inf") else -1
                
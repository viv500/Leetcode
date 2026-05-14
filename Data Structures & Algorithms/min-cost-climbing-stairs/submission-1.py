class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        "can start at index 0 or 1"
        # min cost to get to the ith floor = 
        # min(cost to get to i - 2, cost of i -2, cost to get to i -1, ost of i - 1)
    
        # dp optimization, only need 2 values at a time don't need table
        n = len(cost)
        prev, cur = 0, 0

        for i in range(2, n + 1):
            prev, cur = cur, min(prev + cost[i - 2], cur + cost[i - 1])
            # need to update both at the same time

        return cur


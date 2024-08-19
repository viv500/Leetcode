class Solution:
    def climbStairs(self, n: int) -> int:

        # sub problem: how many ways to get to the nth step

        memo = [0] * (n+1) 

        memo[0] = 1 # 1 way to get 0 steps, do nothing
        memo[1] = 1 # 1 way to get to 1 step, take 1 step

        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]

            

        
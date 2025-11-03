class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''Top-Down	Recursive	Large → Small	recursion + memoization	“Memoized recursion”
            Bottom-Up	Iterative	Small → Large	loops + table	“Tabulation”'''

            # this is a bottom up problem cuz we start with the smallest sub problem
            # theres only 2 possible ways to get to the nth step if step sizes are 1 and 2. either (a) u get to step n -1 and take 1 step, or you get to step n - 2 and take 2 steps. this gives us ways[n] = ways[n - 1] + ways[n - 2]


            # naive sol would make a dp table of dp = [0] * (n - 1) and fill it all the way up. but since we only need 2 results at a time,
            # we dont need a table. so better space efficiency

        
        if(n == 1):
            return 1
        if(n == 2):
            return 2



        temp = 0
        a = 1
        b = 2 # base cases


        for _ in range(n - 2):
            temp = a + b
            a = b
            b = temp

        return temp

        
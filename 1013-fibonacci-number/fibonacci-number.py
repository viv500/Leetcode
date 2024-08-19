class Solution:
    def fib(self, n: int) -> int:
        # memoization
        memo = [0] * (n + 1)

        def fibo(n: int) -> int:

            if n == 1 or n == 2:
                return 1
            if n == 0:
                return 0
            if memo[n] != 0:
                return memo[n]
            memo[n] = fibo(n - 1) + fibo(n - 2)
            return memo[n]

        return fibo(n)




        ''' very inefficient
        if n == 1 or n == 2:
            return 1

        return self.fib(n - 1) + self.fib(n - 2'''
        
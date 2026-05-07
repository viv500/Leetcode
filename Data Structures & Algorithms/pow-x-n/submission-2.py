class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute force is O(n)
        # better solution: O(logn)
        # 2^6 , instead of doing this 6 times (O(n)), we can do 2^3 and square it
        # if 2^7, we can do 2 * (2^3)^2

        def power(x, n):
            if n == 0 : return 1

            half = power(x, n //2)

            if n % 2 == 0: return half * half # for even exponent
            else: return x * half * half # for odd exponent

        # need to handle negative exponent
        if n < 0:
            x = 1/x
            n = -n

        return power(x, n)




       
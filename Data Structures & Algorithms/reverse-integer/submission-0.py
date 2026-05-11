class Solution:
    def reverse(self, x: int) -> int:
        inf, neg_inf = (2**31 - 1), -(2**31)
        num = int(str(abs(x))[::-1])
        sign = 1
        if x < 0: sign = -1
        num *= sign

        return num if neg_inf <= num <= inf else 0

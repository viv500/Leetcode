class Solution:
    def reverse(self, x: int) -> int:
        # O(1) time and space
        maximum, minimum = (2**31 - 1), -(2**31)
        num = int(str(abs(x))[::-1])
        if x < 0: num *= -1

        return num if minimum <= num <= maximum else 0

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            if n == 1: return True
            seen.add(n)

            new = 0
            for c in str(n):
                new += int(c) ** 2

            n = new

        return False

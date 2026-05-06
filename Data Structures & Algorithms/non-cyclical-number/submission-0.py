class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            new = str(n)
            n = 0
            for num in new:
                n += (int(num) ** 2)

            if n in seen: return False
            seen.add(n)

        return True
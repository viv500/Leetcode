class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1: return True
            seen.add(n)
            num = 0
            for digit in str(n):
                num += int(digit) ** 2
            n = num
        return False
            

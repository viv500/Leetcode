class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2**31
        MAX = 2**31 - 1
        s = s.strip()
        if not s: return 0

        isNegative = False
        if s[0] in ("+", "-"):
            if s[0] == "-": isNegative = True
            s = s[1:]

        num = 0

        for i,s in enumerate(s):
            if s.isdigit():
                num = (num * 10) + (ord(s) - ord("0"))
            else:
                break

        return max(MIN, num * -1) if isNegative else min(MAX, num)
            
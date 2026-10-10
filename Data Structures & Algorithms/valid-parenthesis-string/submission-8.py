class Solution:
    def checkValidString(self, s: str) -> bool:
        high = low = 0

        for c in s:
            if c == "(":
                high += 1
                low += 1
            elif c == ")":
                high -= 1
                low -= 1
            else:
                high += 1
                low -= 1

            if high < 0: return False
            low = max(0, low)

        return low == 0
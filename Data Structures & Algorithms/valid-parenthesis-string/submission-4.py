class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0 
        low = 0

        for char in s:
            if char == "(":
                high += 1
                low += 1
            elif char == ")":
                high -= 1
                low -= 1
            elif char == "*":
                low -= 1
                high += 1

            if high < 0: return False
            low = max(low, 0)

        return low == 0
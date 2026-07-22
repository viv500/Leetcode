class Solution:
    def checkValidString(self, s: str) -> bool:
        high, low = 0, 0
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
            
            low = max(low, 0)
            if high < 0: return False
        
        return low == 0
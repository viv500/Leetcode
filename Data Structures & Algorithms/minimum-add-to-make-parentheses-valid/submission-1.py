from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        add = 0
        running = 0

        for c in s:
            running = running + 1 if c == "(" else running - 1
            if running == -1:
                running = 0
                add += 1
        
        return running + add

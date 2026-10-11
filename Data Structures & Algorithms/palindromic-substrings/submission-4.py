class Solution:
    def countSubstrings(self, s: str) -> int:

        def substring_count(i, j):
            count = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]: 
                    count += 1
                    i -= 1
                    j += 1
                else:
                    break
            
            return count

        count = 0
        for i in range(len(s)):
            count += substring_count(i, i)

        for i in range(len(s) - 1):
            count += substring_count(i, i + 1)

        return count
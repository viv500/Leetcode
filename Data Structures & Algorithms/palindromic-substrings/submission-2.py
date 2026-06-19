class Solution:
    def countSubstrings(self, s: str) -> int:
        substring_count = 0
        def substrings(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

            return count

        
        for i in range(len(s)):
            substring_count += substrings(i, i)
            substring_count += substrings(i - 1, i)

        return substring_count
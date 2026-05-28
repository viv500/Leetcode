class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longest_substring = ""
        def expand(i, j):
            nonlocal longest_substring, longest
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            window = j - i + 1
            if window > longest: 
                longest = window
                longest_substring = s[i + 1:j]
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return longest_substring

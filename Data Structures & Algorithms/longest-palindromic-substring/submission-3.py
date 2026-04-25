
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time and O(1) space
        # 1 pass for even length, 1 pass for odd length
        longest = 0
        longest_palindrome = "" 

        def expand(left, right):
            nonlocal longest, longest_palindrome
        
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            length = right - left - 1
            if length > longest:
                # it assumes longest is local cuz of assignment, so non local neede
                longest = length
                longest_palindrome = s[left + 1:right]
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return longest_palindrome

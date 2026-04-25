class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time and O(1) space
        # 1 pass for even length, 1 pass for odd length
        longest = 0
        longest_palindrome = ""
    

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > longest:
                longest = right - left - 1
                longest_palindrome = s[left + 1:right]

        for i in range(len(s)):
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if (right - left - 1) > longest:
                longest = right - left - 1
                longest_palindrome = s[left + 1:right]

        return longest_palindrome

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # odd length pass
        for i in range(len(s)):
            left = right = i
            # counts the individual character as a plaindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -=1
                right += 1

        # even length 
        for i in range(len(s) - 1):
            left = i
            right = i + 1
            # counts the individual character as a plaindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -=1
                right += 1

        return count
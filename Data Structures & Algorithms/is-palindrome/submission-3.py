class Solution:
    def isPalindrome(self, s: str) -> bool:
        # only alphanumeric characters
        new = ""

        # case doesn't matter
        s = s.lower()
        for char in s:
            if char.isalnum():
                new += char

        return new == new[::-1]
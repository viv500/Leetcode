class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                new += i
        return new == new[::-1]
        
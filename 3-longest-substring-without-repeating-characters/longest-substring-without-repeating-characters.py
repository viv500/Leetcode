class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = R = 0
        longest = 0
        chars = set()

        while R < len(s):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            longest = max(longest, R - L + 1)
            chars.add(s[R])

            R += 1
        return longest

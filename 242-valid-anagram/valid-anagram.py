from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = [0] * 26
        freq_t = [0] * 26

        for i in range(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1

        return freq_s == freq_t

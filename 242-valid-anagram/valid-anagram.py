class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        freq_s = [0] * 26
        freq_t = [0] * 26

        for char_s, char_t in zip(s, t):
            freq_s[ord(char_s) - ord('a')] += 1
            freq_t[ord(char_t) - ord('a')] += 1

        return freq_s == freq_t
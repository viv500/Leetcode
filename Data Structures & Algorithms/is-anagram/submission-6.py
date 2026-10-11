class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        f_s = [0] * 26 
        f_t = [0] * 26

        for cs, ct in zip(s, t):
            f_s[ord(cs) - ord('a')] += 1
            f_t[ord(ct) - ord('a')] += 1

        return f_s == f_t
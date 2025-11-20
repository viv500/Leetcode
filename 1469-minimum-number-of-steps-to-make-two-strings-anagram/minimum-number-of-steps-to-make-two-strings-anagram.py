class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = [0] * 26
        freq_t = [0] * 26

        # leetcode l = 1 e = 3 t = 1 c = 1 o = 1 d = 1
        # practice p = 1 e = 1 t = 1 c = 2 i = 1 r = 1 a = 1


        for i in range(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1
        
        total = 0
        for i in range(26):
            if freq_t[i] < freq_s[i]:
                total += (freq_s[i] - freq_t[i])

        return total
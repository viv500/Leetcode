class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = [0] * 26
        t_freq = [0] * 26

        for char in s:
            s_freq[ord('a') - ord(char)] += 1

        for char in t:
            t_freq[ord('a') - ord(char)] += 1

        return s_freq == t_freq
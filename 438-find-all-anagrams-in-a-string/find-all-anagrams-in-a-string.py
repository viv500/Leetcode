class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        result = []
        freq_s = [0] * 26
        freq_p = [0] * 26

        # zip stops at the shorter length
        for char_s, char_p in zip(s, p):
            freq_s[ord(char_s) - ord('a')] += 1
            freq_p[ord(char_p) - ord('a')] += 1


        a, b = 0, len(p)

        while b < len(s):
            if freq_s == freq_p:
                result.append(a)

            freq_s[ord(s[b]) - ord('a')] += 1
            freq_s[ord(s[a]) - ord('a')] -= 1

            a += 1
            b += 1

        
        if freq_s == freq_p:
            result.append(a)

        
        return result


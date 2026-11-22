class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        f1 = [0] * 26
        f2 = [0] * 26
        for c1, c2 in zip(s1, s2):
            f1[ord(c1) - ord('a')] += 1
            f2[ord(c2) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if f1 == f2: return True

            f2[ord(s2[i]) - ord('a')] += 1
            f2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        if f1 == f2: return True

        return False

        


        
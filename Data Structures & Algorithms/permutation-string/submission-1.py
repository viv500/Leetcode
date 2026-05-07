class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        # freq is O(1) space cuz its always size 26
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        left, right = 0, len(s1)

        for i in range(len(s1)):
            freq_s1[ord(s1[i]) - ord('a')] += 1
            freq_s2[ord(s2[i]) - ord('a')] += 1

        while right < len(s2):
            if freq_s1 == freq_s2: return True

            freq_s2[ord(s2[left]) - ord('a')] -= 1
            freq_s2[ord(s2[right]) - ord('a')] += 1

            left += 1
            right += 1

        if freq_s1 == freq_s2: return True

        return False

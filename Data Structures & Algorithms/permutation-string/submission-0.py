class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        # freq is O(1) space cuz its always size 26
        freq_s1 = [0] * 26
        freq_s2 = [0] * 26

        left, right = 0, len(s1)

        for char in s1:
            freq_s1[ord('a') - ord(char)] += 1
        
        for char in s2[:right]:
            freq_s2[ord('a') - ord(char)] += 1

        while right < len(s2):
            if freq_s1 == freq_s2: return True

            freq_s2[ord('a') - ord(s2[left])] -= 1
            freq_s2[ord('a') - ord(s2[right])] += 1

            left += 1
            right += 1

        if freq_s1 == freq_s2: return True

        return False

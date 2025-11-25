class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = R = 0
        longest = 0
        freq = [0] * 26

        while R < len(s):
            freq[ord(s[R]) - ord('A')] += 1

            while((R - L + 1) - max(freq) > k):
                freq[ord(s[L]) - ord('A')] -= 1
                L += 1

            longest = max(longest, R - L + 1)

            R += 1
        return longest

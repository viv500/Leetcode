from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = [0] * 26
        left, right = 0, 0

        while right < len(s):
            freq[ord('A') - ord(s[right])] += 1

            while ((right - left + 1) - max(freq)) > k:
                freq[ord('A') - ord(s[left])] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest
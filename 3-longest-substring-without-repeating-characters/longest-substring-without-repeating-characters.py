class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #sliding window

        left = 0
        chars = set()

        length = len(s)
        longest = 0

        for right in range(length):
            # if our right pointer is on a character that the left wants to include, make the left move right to skip it
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            # if not, keep sliding the window to enlarge, and add right character to set
            chars.add(s[right])
            right += 1

            longest = max(longest, right - left)

        return longest
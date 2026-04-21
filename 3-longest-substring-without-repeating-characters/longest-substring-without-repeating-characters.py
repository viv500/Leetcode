class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # note: we are removing s[left], always exists safe to remove
        # keep removing left characters until we remove the right character that WOULD'VE been a duplicate
        # then, add that right character
        char_set = set()
        longest = 0

        left, right = 0, 0

        while right < len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            longest = max(longest, right - left + 1)

            char_set.add(s[right])

            right += 1
        return longest
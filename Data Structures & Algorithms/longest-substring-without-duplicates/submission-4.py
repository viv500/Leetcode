class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        low = high = 0
        seen = set()

        while high < len(s):
            while s[high] in seen:
                seen.remove(s[low])
                low += 1
            
            longest = max(longest, high - low + 1)
            seen.add(s[high])
            high += 1

        
        return longest

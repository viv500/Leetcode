class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest = 0
        left = right = 0

        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            
            visited.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest

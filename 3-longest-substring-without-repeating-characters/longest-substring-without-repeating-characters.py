class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        L = R = longest = 0
        visited = set()

        while R < len(s):
            while(s[R] in visited):
                visited.remove(s[L])
                L += 1

            visited.add(s[R])
            longest = max(longest, R - L + 1)
            R += 1

        return longest


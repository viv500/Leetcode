class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Q) can s1 be converted into s2 by character mappings. can map to any, character can map to itself, but can't have character map to different characters

        # NEED TO CHECK BOTH WAYS!

        chars = {}
        chart = {}

        if len(s) != len(t): return False

        for index in range(len(s)):
            if s[index] in chars:
                if chars[s[index]] != t[index]: # i.e. if we previously mapped this character to another one
                    return False
            else:
                chars[s[index]] = t[index]

            if t[index] in chart:
                if chart[t[index]] != s[index]: # i.e. if we previously mapped this character to another one
                    return False
            else:
                chart[t[index]] = s[index]

        return True
        
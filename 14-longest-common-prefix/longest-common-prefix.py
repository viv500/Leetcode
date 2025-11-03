class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        result = ""
        smallest = min(len(word) for word in strs)  # find the length of the shortest word

        for i in range(smallest):
            cur = strs[0][i]  # current character to compare
            for word in strs:
                if word[i] != cur:
                    return result
            result += cur

        return result


"""
Explanation:
We compare characters column by column across all strings. 
If all strings share the same character at position i, 
we add it to the result. Otherwise, we stop immediately 
since the common prefix ends there.

Time Complexity: O(n * m) — n = number of strings, m = length of shortest string.
Space Complexity: O(1) — only uses a few variables.

This vertical scanning approach is clear, efficient, and easy to reason about.
"""

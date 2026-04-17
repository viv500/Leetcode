class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:



        # recusive approach : works but TLE
        # this is Top Down DP (memoization)
        # Time and Space: O(m*n)

        i, j = len(text1), len(text2)
        @cache
        def compare(i, j):
            if i == len(text1) or j == len(text2): return 0

            if text1[i] == text2[j]:
                return 1 + compare(i + 1, j + 1)
            else:
                return max(compare(i + 1, j), compare(i, j + 1))

        
        return compare(0, 0)

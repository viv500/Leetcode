from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down (Recursive + Memoization) 
        # O(m * n) time and space
        # acts like a memo dict to remember repeated computations
        @cache


        def longest(i, j):
            if i == len(text1) or j == len(text2): return 0

            if text1[i] == text2[j]:
                return 1 + longest(i + 1, j + 1)
            else:
                return max(longest(i + 1, j), longest(i, j + 1))

        return longest(0, 0)

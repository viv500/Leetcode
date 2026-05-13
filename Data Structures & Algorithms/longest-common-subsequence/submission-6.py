from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top down (Recursive + Memoization) 
        # O(m * n) time and space
        # acts like a memo dict to remember repeated computations
        dp = {}
        def longest(i, j):
            if i == len(text1) or j == len(text2): return 0

            if (i, j) in dp: return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + longest(i + 1, j + 1)
            else:
                dp[(i, j)] = max(longest(i + 1, j), longest(i, j + 1))

            return dp[(i, j)]

        return longest(0, 0)


        # Bottom up (Iterative + Tabulation)
        # O(m * n) time and space

        # extra length needed to represnt base case i.e. the LCS of 2 empty strings
        # here, dp[i][j] = LCS of first i and j chars in text1 and text2 (excluding i and j)
        # extra length allows us to capture the final characters

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # all 0 indices skipped cuz that's the base case
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # dp[i][j] => answer of text1 and 2 upto i - 1 and j - 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1] # moving down the digonal with increments
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)
        return dp[len(text1)][len(text2)]



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Bottom Up DP (Tabulation)
        # Time and Space: O(m*n)
        # 2d dp where dp[i][j] represents the longest subsring that can be formed upto the (i -1)th index of text1 and (j - 1)th index of text2

# text1 = "gators"
# text2 = "agars"
#
#        ""  a  g  a  r  s
#    ""  0   0  0  0  0  0
#    g   0   0  1  1  1  1
#    a   0   1  1  2  2  2
#    t   0   1  1  2  2  2
#    o   0   1  1  2  2  2
#    r   0   1  1  2  3  3
#    s   0   1  1  2  3  4
#
# Final answer (bottom-right): 4

        m, n= len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range (m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]



        # Top Down DP (memoization)
        # Time and Space: O(m*n)

        # Important! TLE if not used
        @cache

        def compare(i, j):
            if i == m or j == n: return 0

            if text1[i] == text2[j]:
                return 1 + compare(i + 1, j + 1)
            else:
                return max(compare(i + 1, j), compare(i, j + 1))

        
        return compare(0, 0)

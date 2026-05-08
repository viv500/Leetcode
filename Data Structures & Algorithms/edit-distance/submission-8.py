class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 3 possible operations - assume i tracks word1 and j tracks word 2
        # and all operations are done to word1
        # insert: (i, j) -> (i, j + 1) (we inserted in word1 a character to match the j in word2, so thats done), but index i still has to be matched
        # delete: (i, j) -> (i + 1, j) (we ignored index i in word 1 (deleted) but still need to match with j)
        # replace: (i, j) -> (i + 1, j + 1) (we replaced to match characters in i and j)

        # insert and delete needed when theres a mismatch in number of characters
        # botto up dp: O(m * n)
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(1 + dp[i][j],  
                                           1 + dp[i + 1][j],
                                           1 + dp[i][j + 1]
                                           )

        return dp[m][n]



        # brute force: O(3 ^ (m + n))
        def compare(i, j):
            if i == len(word1) and j == len(word2): return 0
            if i == len(word1): return len(word2) - j # to handle insertions
            if j == len(word2): return len(word1) - i # to handle deletions

            if word1[i] == word2[j]:
                return compare(i + 1, j + 1) # no operations needed
            else:
                # 3 possible operations if theres a mismatch, all require 1 step
                return min(1 + compare(i + 1, j + 1),  # replace character
                           1 + compare(i + 1, j),      # delete character
                           1 + compare(i, j + 1)       # insert character
                          )

        return compare(0, 0)

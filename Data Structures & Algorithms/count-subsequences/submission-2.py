class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # base cases
        if not s: return 0
        if not t: return 1 # subsequence formed by removing all characters of t

        cache = {}

        def dfs(i, j):
            if j == len(t): return 1 # found the target!
            if i == len(s): return 0 # reached end of s without finding target

            if (i + 1, j + 1) not in cache: cache[(i + 1, j + 1)] = dfs(i + 1, j + 1)
            if (i + 1, j) not in cache: cache[(i + 1, j)] = dfs(i + 1, j)

            if s[i] == t[j]:
                return cache[(i + 1, j + 1)] + cache[(i + 1, j)]
            else:
                return cache[(i + 1, j)]

        return dfs(0, 0)
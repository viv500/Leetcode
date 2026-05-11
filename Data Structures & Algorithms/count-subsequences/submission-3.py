class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # base cases
        if not s: return 0
        if not t: return 1 # subsequence formed by removing all characters of t

        cache = {}

        def dfs(i, j):
            if j == len(t): return 1 # found the target!
            if i == len(s): return 0 # reached end of s without finding target

            if (i, j) in cache: return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j) # even if theres a match, we should still try skipping
                                                                          # ex. rabbbit and rabbit
            else:
                cache[(i, j)] = dfs(i + 1, j)

            # for caching, always return value from cache here
            return cache[(i, j)]

        return dfs(0, 0)
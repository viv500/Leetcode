class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(si, pi):
            if (si, pi) in dp: return dp[(si, pi)]
            if pi == len(p): return si == len(s)
            hasStar = pi + 1 < len(p) and p[pi + 1] == "*"
            if si == len(s): return hasStar and dfs(si, pi + 2)

            pattern, char = p[pi], s[si]
            match = pattern == char or pattern == "."

            if hasStar:
                dp[(si, pi)] = (match and dfs(si + 1, pi)) or dfs(si, pi + 2)
                return dp[(si, pi)]

            dp[(si, pi)] = match and dfs(si + 1, pi + 1)
            return dp[(si, pi)]

        return dfs(0, 0)

            
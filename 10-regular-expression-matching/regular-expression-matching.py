class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(si, pi):
            if pi == len(p): return si == len(s)
            hasStar = pi + 1 < len(p) and p[pi + 1] == "*"
            if si == len(s): return hasStar and dfs(si, pi + 2)

            pattern, char = p[pi], s[si]
            match = pattern == char or pattern == "."

            if hasStar:
                return (match and dfs(si + 1, pi)) or dfs(si, pi + 2)

            return match and dfs(si + 1, pi + 1)

        return dfs(0, 0)

            
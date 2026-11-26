class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # collapse multiple *'s into 1 as they behave the same
        collapsed = []
        for c in p:
            if c == "*" and collapsed and collapsed[-1] == "*":
                continue
            collapsed.append(c)

        p = "".join(collapsed)

        dp = {}

        def dfs(si, pi):
            if (si, pi) in dp: return dp[(si, pi)]
            if si == len(s) and pi == len(p): return True
            if si == len(s): return p[pi] == "*" and dfs(si, pi + 1)
            if pi == len(p): return False

            pattern, char = p[pi], s[si]

            if pattern == "?":
                res = dfs(si + 1, pi + 1)
            elif pattern == "*":
                res = dfs(si + 1, pi) or dfs(si, pi + 1)
            else:
                res = pattern == char and dfs(si + 1, pi + 1)
            
            dp[(si, pi)] = res
            return res

        return dfs(0, 0)



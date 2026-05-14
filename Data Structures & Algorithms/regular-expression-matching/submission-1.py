class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i , j):
            if i == len(s) and j == len(p): return True
            if i == len(s):
                if j < len(p) - 1 and p[j + 1] == "*":
                    return dfs(i, j + 2)
                return False
            
            if j == len(p): return False

            if s[i] == p[j] or p[j] == ".":
                # theres a match
                match = dfs(i + 1, j + 1)
                star = False
                if j < len(p) - 1 and p[j + 1] == "*":
                    star = dfs(i + 1, j) or dfs(i, j + 2)  # ✓ can skip even IF match

                return match or star

            # if there no match and theres a star, skip the pattern
            else:
                if j < len(p) - 1 and p[j + 1] == "*":
                    return dfs(i, j + 2)
                else:
                    return False

            
        return dfs(0, 0)



            
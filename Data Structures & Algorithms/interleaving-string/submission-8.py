class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3: return True
        if len(s1) + len(s2) != len(s3): return False

        dp = {}

        def dfs(i1, i2):
            if i1 + i2 == len(s3): return True

            if (i1, i2) in dp: return dp[(i1, i2)]

            result = False
            i3 = i1 + i2
            if i1 < len(s1) and s1[i1] == s3[i3]:
                result = result or dfs(i1 + 1 , i2)

            if i2 < len(s2) and s2[i2] == s3[i3]:
                result = result or dfs(i1 , i2 + 1)

            dp[(i1, i2)] = result
            return result
        
        return dfs(0, 0)
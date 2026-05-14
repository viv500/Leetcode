class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # !! NOTE: the "number of components" constraint means nothing
        # if you reach the end of both strings, that condition is gaurenteed since you "interleaved"
        if len(s1) + len(s2) != len(s3): return False # this prevents index out of boudns errors
        dp = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2): return True

            if (i, j) in dp: return dp[(i, j)]


            # index condition in case we consumed 1 string both not the other
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j): # 
                dp[(i, j)] = True
                return True # need to return immediately so a future false case doesn't overwrite

            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1): # 
                dp[(i, j)] = True
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)
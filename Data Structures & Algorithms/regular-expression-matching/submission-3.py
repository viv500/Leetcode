class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i , j):
            if i == len(s) and j == len(p): return True # both at end, correct!
            if i == len(s): # only string at end, but pattern has a * which allows us to "zero" it, correct
                return j < len(p) - 1 and p[j + 1] == "*" and dfs(i, j + 2)
            if j == len(p): return False # only pattern at end, wrong

            match = (s[i] == p[j] or p[j] == ".")
            hasStar = j < len(p) - 1 and p[j + 1] == "*"

            # if match, 1. consume 1 character from s and p 2. if star, then expand star, 3. if star, then "zero" the star
            if match:
                return dfs(i + 1, j + 1) or (hasStar and dfs(i + 1, j)) or (hasStar and dfs(i, j + 2))
            else:
                # no match, 1. if star, try "zeroing" 2. if no star, return False
                return hasStar and dfs(i, j + 2)
            
        return dfs(0, 0)



            
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can only move right or down
        # dfs problem, can be improved using a DP cache to store previous results
        # if 2 paths are exactly same except for their first decision, dfs will have more calculations involves than dp
        # dp relation: start from bottom right corner
        # - for each cell, number of ways to get there = number of ways to get to the cell to the right + down (if inside the grid)

        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if (row, col) == (m - 1, n - 1): continue

                cell_value = 0
                # has right cell?
                if col + 1 < n:
                    cell_value += dp[row][col + 1]

                if row + 1 < m:
                    cell_value += dp[row + 1][col]

                dp[row][col] = cell_value

        return dp[0][0]

# Time: O(m*n), Space: O(m*n)
# Space can be optimized further by using a 1d table since we only ever need 2 values at a time
                


# Standard DFS - Works but not efficient enough due to multiple duplicate calculations
'''
        paths = 0
        # Must declare it as nonlocal to tell Python not to treat it as local.
    

        def dfs(r, c):
            nonlocal paths
            if r >= m or c >= n or r < 0 or c < 0: return

            if (r, c) == (m - 1, n - 1):
                paths += 1

            dfs(r + 1, c)
            dfs(r, c + 1)

        
        dfs(0, 0)
        return paths
        '''
        
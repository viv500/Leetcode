class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute force: recursive/decision tree - O(m * n * 4 ^(m*n))
        rows, cols = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = {} # (r, c) -> LIS that starts at (r, c)
        def dfs(r, c, prevVal):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prevVal:
                return 0
            
            if (r, c) in dp: 
                return dp[(r, c)]

            value = matrix[r][c]

            dp[(r, c)] = max(1 + dfs(r - 1, c, value), 
                       1 + dfs(r, c - 1, value), 
                       1 + dfs(r + 1, c, value), 
                       1 + dfs(r, c + 1, value))

            return dp[(r, c)]

        
        LIS = 0
        for row in range(rows):
            for col in range(cols):
                LIS = max(LIS, dfs(row, col, float("-inf")))

        return LIS            
            
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        self.longest = 0
        dp = {}

        def dfs(r, c, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev: return 0

            if (r, c) in dp: return dp[(r, c)]

            v = matrix[r][c]

            dp[(r, c)] =  1 + max(dfs(r + 1, c, v), dfs(r - 1, c, v), dfs(r, c + 1, v), dfs(r, c - 1, v))

            return dp[(r, c)]

        for row in range(rows):
            for col in range(cols):
                self.longest = max(self.longest, dfs(row, col, float("-inf")))

        return self.longest


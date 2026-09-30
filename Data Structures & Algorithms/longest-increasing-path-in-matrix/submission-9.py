class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev: return 0

            if (r, c) in dp: return dp[(r, c)]
            val = matrix[r][c]
            dp[(r, c)] =  1 + max(dfs(r + 1, c, val), dfs(r - 1, c, val), dfs(r, c + 1, val), dfs(r, c - 1, val))

            return dp[(r, c)]

        max_length = 0
        for row in range(rows):
            for col in range(cols):
                max_length = max(max_length, dfs(row, col, float("-inf")))

        return max_length
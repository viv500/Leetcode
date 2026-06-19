class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.longest = {}
        self.result = 0

        def search(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev: return 0
            if (r, c) in self.longest: return self.longest[(r, c)]

            value = matrix[r][c]
            self.longest[(r, c)] = 1 + max(search(r + 1, c, value), search(r, c + 1, value), search(r - 1, c, value), search(r, c - 1, value))

            return self.longest[(r, c)]

        
        for row in range(rows):
            for col in range(cols):
                self.result = max(self.result, search(row, col, -1))

        return self.result

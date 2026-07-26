# area of rectange = 
# bottom right corner rectangle - top bonudary rectangle - left boundary rectangle + top left square that was minused twice


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = matrix

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if i - 1 >= 0: self.dp[i][j] += self.dp[i - 1][j] # above
                if j - 1 >= 0: self.dp[i][j] += self.dp[i][j- 1] # left
                if i - 1 >= 0 and j - 1 >= 0: self.dp[i][j] -= self.dp[i - 1][j - 1] # remove overlap


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        dp = self.dp

        total = dp[row2][col2]
        if row1 - 1 >= 0: total -= dp[row1 - 1][col2]
        if col1 - 1 >= 0: total -= dp[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0: total += dp[row1 - 1][col1 - 1]

        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 90 degrees clockwise: tranpose then reverse rows
        # 90 degrees counter clocokwise: reverse rows then transpose

        # for transpose, should only flip 1 half triangle of the square, if not, everything gets flipped twice
        # which gives us back the original matrix

        rows = len(matrix)

        for row in range(rows):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


        for row in matrix:
            row.reverse()
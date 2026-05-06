class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # use an indicator to clear rows so we don't overwrite information
        # 0th row and 0th col are indicators
        # maintain a vairable to track if row or col triggered [0][0] to be marked

        rows, cols = len(matrix), len(matrix[0])
        clearFirstRow = False
        clearFirstCol = False

        # mark rows and cols
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = "!"
                    matrix[row][0] = "!"

                    if row == 0: clearFirstRow = True
                    if col == 0: clearFirstCol = True

        # clear rows
        for row in range(1, rows):
            if matrix[row][0] == "!":
                matrix[row] = [0] * cols
        
        # clear cols
        for col in range(1, cols):
            if matrix[0][col] == "!":
                for i in range(rows):
                    matrix[i][col] = 0

        # clear first row
        if clearFirstRow:
            matrix[0] = [0] * cols

        # clear first column
        if clearFirstCol:
            for row in range(rows):
                matrix[row][0] = 0


        print(matrix)
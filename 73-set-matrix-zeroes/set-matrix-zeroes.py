class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # can't set 1->0 within loop since it may set others ones to 0 prematurely (which means we won't clear their rows' and columns' 1s to 0s)


        # can't use markers for this cuz we wouldn't know if it was marked by the row or column
        # the cell on the first row, first column is the only overlap
        # still O(1)
        clearFirstRow = False
        clearFirstCol = False

        rows, cols = len(matrix), len(matrix[0])

        # marking the first element of each row and each column -> should get cleared next
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0: clearFirstRow = True
                    if col == 0: clearFirstCol = True

                    matrix[0][col] = "!"
                    matrix[row][0] = "!"

        print(matrix)
        
        for row in range(1, rows):
            if matrix[row][0] == "!":
                for col in range(cols):
                    matrix[row][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == "!":
                for row in range(rows):
                    matrix[row][col] = 0

        if clearFirstRow:
            for col in range(cols):
                matrix[0][col] = 0

        if clearFirstCol:
            for row in range(rows):
                matrix[row][0] = 0




        print(matrix)
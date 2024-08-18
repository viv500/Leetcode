class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        transpose = []

        # what each sorted row and column needs to look like
        numbers = [i for i in range(1, len(matrix) + 1)]


        # transposing the matrix
        for i in range(len(matrix[0])):  # Iterate over columns
            sub = []  # Initialize a new row for the transpose
            for j in range(len(matrix)):  # Iterate over rows
                sub.append(matrix[j][i])  # Append the element from the current row and column
            transpose.append(sub)  # Add the new row to the transpose matrix

        # check rows 
        for i in matrix:
            if sorted(i) != numbers:
                return False

        # check columns
        for i in transpose:
            if sorted(i) != numbers:
                return False

        # good to go
        return True

        
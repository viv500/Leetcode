class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows, 0, cols
        output = []

        while top < bottom and left < right:

            # left to right
            for i in range(left, right):
                output.append(matrix[top][i])
            
            top += 1

            # top to bottom
            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            
            right -= 1

            # right to left
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    output.append(matrix[bottom - 1][i])
            
                bottom -= 1

            # bottom to top
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    output.append(matrix[i][left])
            
                left += 1

        return output

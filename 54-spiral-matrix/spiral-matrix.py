class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        result = []

        while left <= right and top <= bottom:
            # left -> right
            for c in range(left, right + 1):
                result.append(matrix[top][c])

            top += 1

            # top -> bottom
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])

            right -= 1


            if top <= bottom:
                # right -> left
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])

                bottom -= 1 


            if left <= right:
                # bottom -> top
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])

                left += 1 

        return result

            


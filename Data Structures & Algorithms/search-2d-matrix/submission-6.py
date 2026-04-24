class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # regular search is O(m * n)

        # sorting is top to bottom, left to right
        # binary search on array indices
        # O(log (m * n))

        # mappings: 
        # flatenned index = ((rows) * r) + c
        # r = (flattened index // cols),  c = (flattened index % rows)  

        # note: "row/col" used for 2d representation
        #       "index" used for flatenned 1d reprsentation

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = (high + low) // 2

            middle_row = mid // cols
            middle_col = mid % cols

            number = matrix[middle_row][middle_col]

            if number == target:
                return True
            elif number > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False



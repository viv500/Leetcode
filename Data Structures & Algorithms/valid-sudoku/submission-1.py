class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.': continue

                if value in row_set[row]: return False
                row_set[row].add(value)

                if value in col_set[col]: return False
                col_set[col].add(value)

                box_index = ((row // 3) * 3) + (col // 3)
                if value in box_set[box_index]: return False
                box_set[box_index].add(value)

        return True

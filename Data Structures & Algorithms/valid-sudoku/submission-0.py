class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box index logic: (r // 3) * 3 + (c // 3)
        # r // 3 places each row into row 0, 1, or 2
        # the *3 accounts is cuz each row has 3 boxes (so box 0, 3, 6)
        # + (c // 3) to move horizontally (ex box 1, 4, 7)

        # 0 1 2
        # 3 4 5
        # 6 7 8
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                number = board[row][col]

                if number == ".": continue

                if number in rows[row]: return False
                rows[row].add(number)

                if number in cols[col]: return False
                cols[col].add(number)

                box_index = ((row // 3) * 3) + (col // 3)

                if number in boxes[box_index]: return False
                boxes[box_index].add(number)

        return True



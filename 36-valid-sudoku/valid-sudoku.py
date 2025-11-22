class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in rows[r]:
                    return False
                rows[r].add(cell)

                if cell in cols[c]:
                    return False
                cols[c].add(cell)

                box_index = (r // 3) * 3 + (c // 3)

                if cell in boxes[box_index]:
                    return False
                boxes[box_index].add(cell)

        return True
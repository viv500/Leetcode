from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 
        rows, cols = len(board), len(board[0])
        border_cells = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                # Top & Bottom row
        for col in range(cols):
            if board[0][col] == "O":
                board[0][col] = "*"
                border_cells.append((0, col))

            if board[rows - 1][col] == "O":
                board[rows - 1][col] = "*"
                border_cells.append((rows - 1, col))

        # Left & Right column
        for row in range(rows):
            if board[row][0] == "O":
                board[row][0] = "*"
                border_cells.append((row, 0))

            if board[row][cols - 1] == "O":
                board[row][cols - 1] = "*"
                border_cells.append((row, cols - 1))


        while border_cells:
            r, c = border_cells.pop()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "*"
                    border_cells.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "*":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
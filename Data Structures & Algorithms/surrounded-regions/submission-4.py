from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque()

        # call bfs on every edge O cell. all remaining O's are surrounded
        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0 or row == rows - 1 or col == cols - 1) and board[row][col] == "O":
                    board[row][col] = "!"
                    q.append((row, col))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    board[nr][nc] = "!"
                    q.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "!":
                    board[row][col] = "O"
    
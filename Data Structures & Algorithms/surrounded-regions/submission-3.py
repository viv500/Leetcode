class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # any "O" component that is connected to the border is NOT surrounded
        # if the component is NOT connected to the border, it should be flipped
        # run a dfs/bfs on all border "O"s

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] != "O":
                return

            visited.add((r, c))

            board[r][c] = "*"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # top and bottom border
        for col in range(cols):
            if board[0][col] == "O": dfs(0, col)
            if board[rows - 1][col] == "O": dfs(rows - 1, col)
        
        # left and right border
        for col, row in enumerate(board):
            if row[0] == "O": dfs(col, 0)
            if row[cols - 1] == "O": dfs(col, cols - 1)

        # flip all surrounded X's to O's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O": board[row][col] = "X"

        # reset all stars to "non-surrounded" X's
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "*": board[row][col] = "O"
            
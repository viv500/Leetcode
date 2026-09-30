class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(r, c, index):
            if index == len(word): return True
            if (r, c) in path or r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]: return False

            path.add((r, c))
            found = dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1) or dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1)
            path.remove((r, c))

            return found

        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0): return True

        return False

        
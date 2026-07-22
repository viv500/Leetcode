class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()


        def dfs(r, c, index):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] != word[index]:
                return False

            visited.add((r, c))

            if index == len(word) - 1:
                return True

            value = dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1)

            visited.remove((r, c))

            return value


        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0): return True

        return False
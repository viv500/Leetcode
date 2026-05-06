class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        rows, cols = len(board), len(board[0])

        def dfs(index, r, c):
            if index == len(word): return True

            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in path or board[r][c] != word[index]: return False

            path.add((r, c))
            # need to collect result and no return now cuz we need to backtrack first
            result = dfs(index + 1, r, c + 1) or dfs(index + 1, r + 1, c) or dfs(index + 1, r - 1, c) or dfs(index + 1, r, c - 1)
            path.remove((r, c))

            return result

        
        for row in range(rows):
            for col in range(cols):
                if dfs(0, row, col): return True
        
        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        path = set()

        def dfs(r, c, i):

            if i == len(word):
                return True

            # all the cases where neighbouring element either goes out of bounds, isn't what we are looking
            # for, or we've already used it
            if (r >= ROWS or c >= COLS or c < 0 or r < 0 or word[i] != board[r][c] or (r, c) in path):
                return False

            path.add((r, c))

            result = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            # backtrack to remove the path we just added to explore other possibilities

            path.remove((r, c))

            return result
        
        # call dfs for every element

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False



        
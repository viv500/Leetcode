class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # can try all n positions on each row
        # don't need a row set cuz we're iterating through each row and placing exactly 1 queen on each row

        # every col and row can be 0-indexed
        # positive rows have a constant r + c (bottom to top, left to right)
        # negative rows have a constant r - c (top to bottom, left to right)
        # number of positive and negative diagonals are 2 * n - 1
        colSet = set() # c
        posDiagSet = set() # r + c
        negDiagSet = set() # r - c
        queens = []
        positions = []

        def dfs(positions, row):
            if len(positions) == n:
                queens.append(positions.copy())
                return
            if row >= n : return

            for col in range(n):
                if (col not in colSet) and (row + col not in posDiagSet) and (row - col not in negDiagSet):
                    colSet.add(col)
                    posDiagSet.add(row + col)
                    negDiagSet.add(row - col)
                    positions.append([row, col])

                    dfs(positions, row + 1) 

                    colSet.remove(col)
                    posDiagSet.remove(row + col)
                    negDiagSet.remove(row - col)
                    positions.pop()
        
        dfs([], 0)

        results = [[] for _ in range(len(queens))]
        for i, board in enumerate(queens):
            for row, col in board:
                before = col
                after = n - col - 1
                results[i].append("." * before + "Q" + "." * after)
        

        return results

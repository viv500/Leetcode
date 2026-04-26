class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # can try all n positions on each row
        # don't need a row set cuz we're iterating through each row and placing exactly 1 queen on each row

        # every col and row can be 0-indexed
        # positive rows have a constant r + c (bottom to top, left to right)
        # negative rows have a constant r - c (top to bottom, left to right)
        # number of positive and negative diagonals are 2 * n - 1
        colSet, posDiagSet, negDiagSet = set(), set(), set()
        positions = []  # positions[r] = col of queen in row r
        results = []

        def dfs(row):
            if row == n:
                results.append(["." * c + "Q" + "." * (n - c - 1) for c in positions])
                return

            for col in range(n):
                if col in colSet or (row + col) in posDiagSet or (row - col) in negDiagSet:
                    continue
                colSet.add(col)
                posDiagSet.add(row + col)
                negDiagSet.add(row - col)
                positions.append(col)

                dfs(row + 1)

                colSet.remove(col)
                posDiagSet.remove(row + col)
                negDiagSet.remove(row - col)
                positions.pop()

        dfs(0)
        return results

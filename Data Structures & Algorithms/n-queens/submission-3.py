class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        path = []
        col_set = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(row):
            if row == n: 
                output.append(path.copy())
                return

            for col in range(n):
                lay = ("." * col) + "Q" + ("." * (n - col - 1))
                if col not in col_set and row + col not in pos_diag and row - col not in neg_diag:
                    col_set.add(col)
                    pos_diag.add(col + row)
                    neg_diag.add(row - col)

                    path.append(lay)
                    backtrack(row + 1)
                    path.pop()

                    col_set.remove(col)
                    pos_diag.remove(row + col)
                    neg_diag.remove(row - col)


        backtrack(0)
        return output

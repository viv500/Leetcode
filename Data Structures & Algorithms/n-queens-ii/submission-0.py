
# building the boards are a waste of space if we only need a count
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.solutions = 0

        pDiagSet = set()
        nDiagSet = set()
        colSet = set()
        def backtrack(row):
            if row == n:
                self.solutions += 1
                return
            
            for col in range(n):
                pDiag = row + col
                nDiag = row - col

                if col not in colSet and pDiag not in pDiagSet and nDiag not in nDiagSet:
                    colSet.add(col)
                    pDiagSet.add(pDiag)
                    nDiagSet.add(nDiag)

                    backtrack(row + 1)

                    colSet.remove(col)
                    pDiagSet.remove(pDiag)
                    nDiagSet.remove(nDiag)

        backtrack(0)
        return self.solutions
            

            

        
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = [set() for _ in range(n)]
        positive_diagonal_set = [set() for _ in range(2 * n - 1)]
        negative_diagonal_set = [set() for _ in range(2 * n - 1)]

        output = []
        solution = []
        def backtrack(row):
            if row == n:
                output.append(solution.copy())
                return

            for col in range(n):
                if not col_set[col] and not positive_diagonal_set[row + col] and not negative_diagonal_set[row - col]:
                    col_set[col].add(row)
                    positive_diagonal_set[row + col].add(row)
                    negative_diagonal_set[row - col].add(row)

                    solution.append(("." * col) + "Q" + ("." * (n - col - 1)))

                    backtrack(row + 1)

                    solution.pop()

                    col_set[col].remove(row)
                    positive_diagonal_set[row + col].remove(row)
                    negative_diagonal_set[row - col].remove(row)

        backtrack(0)
        return output

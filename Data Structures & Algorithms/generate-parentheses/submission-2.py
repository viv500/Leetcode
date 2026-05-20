class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        parentheses = []

        def backtrack(count, diff):
            if count == n and diff == 0:
                output.append(parentheses.copy())
                return

            if count < n:
                parentheses.append("(")
                backtrack(count + 1, diff + 1)
                parentheses.pop()

            if diff >= 1:
                parentheses.append(")")
                backtrack(count, diff - 1)
                parentheses.pop()
               

        backtrack(0, 0)

        return [''.join(string) for string in output]



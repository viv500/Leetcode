class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def backtrack(count, diff):
            if count == n and diff == 0:
                result.append("".join(path))
                return

            if count < n:
                path.append("(")
                backtrack(count + 1, diff + 1)
                path.pop()

            if diff > 0:
                path.append(")")
                backtrack(count, diff - 1)
                path.pop()


        backtrack(0, 0)
        return result
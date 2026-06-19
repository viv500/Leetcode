class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        string = []

        def backtrack(diff, count):
            if diff == 0 and count == n:
                output.append("".join(string))
                return

            if diff > 0:
                string.append(")")
                backtrack(diff - 1, count)
                string.pop()
            
            if count < n:
                string.append("(")
                backtrack(diff + 1, count + 1)
                string.pop()

        backtrack(0, 0)
        return output
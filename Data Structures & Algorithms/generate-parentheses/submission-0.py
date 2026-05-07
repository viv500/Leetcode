class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        string = []

        def backtrack(count, diff):
            if count == n and diff == 0:
                output.append("".join(string))

            if count < n: 
                string.append("(")
                backtrack(count + 1, diff + 1)
                string.pop()

            if diff > 0:
                string.append(")")
                backtrack(count, diff - 1)
                string.pop()
            


        backtrack(0, 0)
        

        return output
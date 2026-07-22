class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        paren = []
        def backtrack(count, diff):
            if count == n and diff == 0:
                result.append("".join(paren))
                return
    
            if count < n:
                paren.append("(")
                backtrack(count + 1, diff + 1)
                paren.pop()
            
            if diff > 0:
                paren.append(")")
                backtrack(count, diff - 1)
                paren.pop()

        backtrack(0, 0)
        return result
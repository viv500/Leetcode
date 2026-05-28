class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        string = []

        def generate(diff, count):
            if count == n and diff == 0:
                output.append(''.join(string))
            
            if diff > 0:
                string.append(")")
                generate(diff - 1, count)
                string.pop()

            if count < n:
                string.append("(")
                generate(diff + 1, count + 1)
                string.pop()
        
        generate(0, 0)
        return output


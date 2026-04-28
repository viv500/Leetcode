class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if token in ("+", "-", "/", "*"):
                # guarenteed for stack to have at least 2 numbers if we see an op
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            # number
            else: stack.append(int(token))

        
        return(stack[0])
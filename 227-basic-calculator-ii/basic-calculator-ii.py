class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        s.strip()
        prev_op = "+"

        for c in (s + "+"):
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == " ":
                continue

            # operands left
            else:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    top = stack.pop()
                    stack.append(top * num)
                else: # /
                    top = stack.pop()
                    stack.append(int(top / num))

                prev_op = c
                num = 0

        return sum(stack)



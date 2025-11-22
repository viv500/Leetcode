class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c) # takes care of multi digit numbers
            elif c == "+":
                ans += num * sign
                # reset sign
                sign = 1
                num = 0
            elif c == "-":
                ans += num * sign
                # reset sign
                sign = -1
                num = 0
            elif c == "(":

                stack.append(ans)
                stack.append(sign)
                # reset sign
                sign = 1
                ans = 0
            elif c == ")":
                ans += num * sign
                num = 0
                
                prev_sign = stack.pop()
                prev_ans = stack.pop()

                ans = prev_ans + prev_sign * ans


        ans += num * sign
        return ans


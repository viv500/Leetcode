class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        result = []

        for c in s:
            print(stack)
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c == "[":
                stack.append(str(num))
                num = 0
            elif c == "]":
                new = []
                while not stack[-1].isdigit():
                    new.append(stack.pop())
                
                count = stack.pop()
                new = new[::-1] * int(count)
                stack.append("".join(new))
                
            else:
                stack.append(c)
                
        return "".join(stack)
        





class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                cur = ""
                while stack and stack[-1] != "[":
                    # order here matters
                    cur = stack.pop() + cur
                # this is the [
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * cur)

        return ''.join(stack)
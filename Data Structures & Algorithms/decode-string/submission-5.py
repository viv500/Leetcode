class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0

        while index < len(s):
            if s[index].isdigit():
                number = s[index]
                index += 1

                while index < len(s) and s[index].isdigit():
                    number += s[index]
                    index += 1
                
                stack.append(number)
            elif s[index].isalpha():
                stack.append(s[index])
            elif s[index] == "]":
                string = ""
                while not stack[-1].isdigit():
                    string = stack.pop() + string
                
                count = int(stack.pop())
                stack.append(count * string)


            index += 1
            
        return "".join(stack)
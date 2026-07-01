class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                char = ""
                # all letter characters
                while stack[-1] != "[":
                    char = stack.pop() + char
                
                # get rid of the [ from the stack
                stack.pop()
            
                
                count = ""
                # all remainign characters after [ are the count
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                   
                # has to be digit here
                mult = int(count)
                char *= mult


     
            stack.append(char)
    
        return "".join(stack)
            
        
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        hashmap = {")": "(", "}": "{", "]": "["}
        
        for i in s:
            if i in "{[(":
                stack.append(i)
            elif i in hashmap:
                # Check if the stack is empty or top of stack does not match
                if not stack or stack[-1] != hashmap[i]:
                    return False
                stack.pop()
        
        return len(stack) == 0

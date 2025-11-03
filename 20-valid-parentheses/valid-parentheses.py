class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        

        # stack pushing and popping

        stack = []
        # has to be inverted brackets in dict so we can lookup the opening
        matching = {"]": "[", "}": "{", ")": "("}

        for char in s:
            if(char in ["(", "[", "{"]):
                # no push function
                stack.append(char)
            else:
                # need to check if stack is empty, if so its an immediate fail
                if (not stack or stack[-1] != matching[char]):
                    return False
                stack.pop()

        return not len(stack)
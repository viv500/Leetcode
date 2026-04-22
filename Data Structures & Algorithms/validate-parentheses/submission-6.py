class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'}': '{', ']': '[', ')': '('}

        for bracket in s:
            if bracket in ['{', '[', '(']:
                stack.append(bracket)
            else:
                if stack and stack[-1] == matching[bracket]:
                    stack.pop()
                else:
                    return False

        return not stack
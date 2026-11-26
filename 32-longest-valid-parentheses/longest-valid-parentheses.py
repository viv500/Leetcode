# stack has 2 roles 1. tracking non closed brackets and 2. tracking where a valid sequence starts
# this could involve storing the index of a characver not involved in the valid sequence
# length = i - stack[-1]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # we want the first boundary to be -1 so () would be 1 - (-1) = 2
        longest = 0
        for index, c in enumerate(s):
            if c == "(": 
                stack.append(index)
            elif c == ")":
                stack.pop()
                if not stack:
                    stack.append(index) #add the boundary back
                else:
                    longest = max(longest, index - stack[-1])
 
        return longest

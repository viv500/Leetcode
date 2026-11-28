# .split(char) will add a "" entry if theres no space between 2 of the delimiters
# ex. "///".split("/") has 4 ""'s
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for p in path:
            if p == "." or not p: continue
            elif p == "..":
                if stack: stack.pop()
            else: stack.append(p)

        return "/" + "/".join(stack)
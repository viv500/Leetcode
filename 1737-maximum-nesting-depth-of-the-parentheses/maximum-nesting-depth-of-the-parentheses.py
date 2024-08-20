class Solution:
    def maxDepth(self, s: str) -> int:
        mx = 0
        count = 0

        for i in s:
            if i == "(":
                count += 1
                if count > mx:
                    mx = count
            elif i == ")":
                count -= 1
            else:
                continue

        return mx

        
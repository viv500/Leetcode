class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        n = columnNumber
        while n > 0:
            n -= 1
            n, remain = divmod(n, 26)
            result.append(chr(ord("A") + remain))


        return "".join(result)[::-1]
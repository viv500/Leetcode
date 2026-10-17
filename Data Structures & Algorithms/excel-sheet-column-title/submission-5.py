class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        n = columnNumber
        while n > 0:
            n -= 1 # column tiles are 1-indexed, so we need to normalize cuz divmod assumes 0
            n, remain = divmod(n, 26)
            result.append(chr(ord("A") + remain))


        return "".join(result)[::-1]
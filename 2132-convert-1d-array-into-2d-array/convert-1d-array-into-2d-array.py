class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        new = []
        p = 0
        while p < len(original):
            new.append(original[p:p + n])
            p += n

        return new
        
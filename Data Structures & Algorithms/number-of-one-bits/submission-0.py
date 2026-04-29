class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            isOne = n & 1

            if isOne: count += 1

            n = n >> 1

        return count
class Solution:
    def reverseBits(self, n: int) -> int:
        # & (AND) 1 capctures the right most bit, ex 10110101 & 00000001
        # | (OR) can be used to turn a specific bit ON (1) ex 10101 | 01000
        # incies in binary are counted from right to left

        result = 0

        for i in range(32):
            bit = (n >> i) & 1  # moves ith bit to the right and captures

            if bit == 1:
                result |= (1 << (31 - i))

        return result
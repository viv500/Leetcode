class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            one_bits = 0
            number = i
            for _ in range(32):
                one_bits += (number & 1)
                number >>= 1

            output[i] = one_bits

        return output
                
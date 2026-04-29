class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n + 1):
            one_count = 0

            for _ in range(32):
                one_count += (num & 1)
                num = num >> 1
            
            output.append(one_count)
            one_count = 0

        return output
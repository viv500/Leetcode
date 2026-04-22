class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # "no extra space": can't use hashmap or set

        # XORing 2 numbers always = 0
        # XORing all pairs of duplicates = 0, and XORing these 0s = 0
        # XORing a number with 0 = the number
        # XOR is associative and commutative
        # we can find the number that only appears once!

        res = 0
        for num in nums:
            res ^= num

        return res
        
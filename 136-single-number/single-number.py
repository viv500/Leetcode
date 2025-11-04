class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Same numbers XOR to zero: a ^ a = 0
        # XOR with zero returns original: a ^ 0 = a
        # Commutative: a ^ b = b ^ a
        # Associative: (a ^ b) ^ c = a ^ (b ^ c)


        # if you xor every number in the list, if all of them but 1 have a duplicate,
        # the expression will be simplified to 0 ^ a, which gives a


        ans = 0

        for num in nums:
            ans ^= num

        return ans

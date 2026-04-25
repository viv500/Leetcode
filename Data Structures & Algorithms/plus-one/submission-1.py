class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(n) time and O(1) spce
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # got to the start and need to add extra 1
        return [1] + digits
        
        # heavy conversions but O(n) time and O(n) space
        digits = [str(d) for d in digits]
        digits = "".join(digits)
        digits = str(int(digits) + 1)
        digits = list(digits)
        digits = [int(d) for d in digits]  
        
        return digits
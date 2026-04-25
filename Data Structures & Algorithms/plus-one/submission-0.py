class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        digits = "".join(digits)
        digits = str(int(digits) + 1)
        digits = list(digits)
        digits = [int(d) for d in digits]  
        
        return digits
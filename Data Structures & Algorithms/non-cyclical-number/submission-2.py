class Solution:
    def isHappy(self, n: int) -> bool:
        number_set = set()
        number = 0
        for digit in str(n):
            number += int(digit) ** 2

        while number != 1 and number not in number_set:
            number_set.add(number)
            new_number = 0

            for digit in str(number):
                new_number += int(digit) ** 2
            
            number = new_number
        
        return number == 1
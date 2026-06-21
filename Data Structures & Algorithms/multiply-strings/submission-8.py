class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # position of j in num2 decides where the product starts
        # position of i in num1 decides how much to the left that product goes

        #   "123" 
        #   "456"
        # xxxxxx

        # i = 2 j = 2 k = 5 
        # i = 1 j = 0 k = 2
        # i = 0 j = 0 k = 1
        # i = 1 j = 1 k = 3

        output = [0] * (len(num1) + len(num2))

        for i in range(len(num2) - 1, -1, -1):
            for j in range(len(num1) - 1, -1, -1):
                index = i + j + 1
                product = int(num2[i]) * int(num1[j])

                value = output[index] + product
                first_digit, second_digit = value // 10, value % 10
                
                output[index] = second_digit
                output[index - 1] += first_digit

        return "".join(map(str, output)).lstrip("0") or "0"
